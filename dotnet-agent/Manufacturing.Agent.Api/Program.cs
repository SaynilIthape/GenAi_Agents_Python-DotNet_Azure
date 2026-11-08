using System.Diagnostics;
using Manufacturing.Agent.Api.Agents;
using Manufacturing.Agent.Api.Contracts;
using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;
using OllamaSharp;
using Manufacturing.Agent.Api.Infrastructure.Rag;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
// builder.Services.AddOpenApi();

var endpoint = builder.Configuration["AI:Ollama:Endpoint"]   ?? "http://localhost:11434";
var model = builder.Configuration["AI:Ollama:Model"]   ??  "llama3.2:3b";
var ragEndPoint =  builder.Configuration["AI:Rag:Endpoint"]?? "http://localhost:8000";

builder.Services.AddHttpClient<RagClinet>(client =>
    {
          client.BaseAddress = new Uri(ragEndPoint);
          client.Timeout = TimeSpan.FromSeconds(60);
    });



builder.Services.AddSingleton<IChatClient>(_=> new OllamaApiClient(new Uri(endpoint),model));

builder.Services.AddSingleton<AIAgent>(s =>
{
    
    var chatclient = s.GetRequiredService<IChatClient>();
    return chatclient.AsAIAgent(
        name: "MachineDiagnosticAgent",
          instructions: """
            You are an expert manufacturing machine
            diagnostic assistant.

            Provide evidence-aware preliminary assessments.
            Prioritize operational safety.
            Never invent machine-specific information.
            """
    );
});

builder.Services.AddSingleton<MachineDiagnosticAgent>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

app.MapGet("/weatherforecast", () =>
{
    var forecast =  Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast
        (
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            summaries[Random.Shared.Next(summaries.Length)]
        ))
        .ToArray();
    return forecast;
})
.WithName("GetWeatherForecast");

app.MapGet("/health", () =>
    Results.Ok(new { status = "Healthy" })
    );

app.MapPost("/api/diagnostics",async (DiagnosticRequest request,
MachineDiagnosticAgent agent,CancellationToken cancellationToken)=>
{
   
  var machineId = request.MachineId?.Trim();
  var observedCondition =  request.ObservedCondition?.Trim();

  if(string.IsNullOrWhiteSpace(machineId) || string.IsNullOrWhiteSpace(observedCondition) )
    return Results.BadRequest(new
        {
            error = "MachineId and ObservedCondition are required."
    });

    if (machineId.Length > 50 ||
        observedCondition.Length > 2000)
    {
        return Results.BadRequest(new
        {
            error = "Input exceeds the permitted length."
        });
    }
    var response = await agent.DiagnoseAsync(machineId,observedCondition,cancellationToken:cancellationToken);
    
    return Results.Ok(response);
 
});

app.Run();

record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
