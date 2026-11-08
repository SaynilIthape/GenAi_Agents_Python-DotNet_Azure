

namespace Manufacturing.Agent.Api.Infrastructure.Rag;

public class RagClinet
{
    private readonly ILogger<RagClinet> _ilogger;
    private readonly HttpClient _client;
    public RagClinet(HttpClient client, ILogger<RagClinet> logger)
    {
        _ilogger=logger;
        _client=client;
    }

    public async Task<RagQueryResponse> AskAsync( string question,
        string machineId,
        CancellationToken cancellationToken)
    {
        var request = new RagQueryRequest
        {
             Question = question,
             MachineId = machineId
        };

                 _ilogger.LogInformation(
            "Calling Python RAG for machine {MachineId}",
            machineId);

        var response =  await _client.PostAsJsonAsync("/ask",
            request,
            cancellationToken:cancellationToken);
        
        response.EnsureSuccessStatusCode();

        var result =  await response.Content.ReadFromJsonAsync<RagQueryResponse>(cancellationToken: cancellationToken);
        
        return result
            ?? throw new InvalidOperationException(
                "Python RAG returned an empty response.");

    } 
}