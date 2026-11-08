using System.Reflection.PortableExecutable;
using Manufacturing.Agent.Api.Contracts;
using Manufacturing.Agent.Api.Infrastructure.Rag;
using Microsoft.Agents.AI;

namespace Manufacturing.Agent.Api.Agents;

public sealed class MachineDiagnosticAgent
{
    private readonly AIAgent _aiAgent;
    private ILogger<MachineDiagnosticAgent> _logger;
    private readonly RagClinet ragClinet;

    public  MachineDiagnosticAgent(AIAgent agent,RagClinet client, ILogger<MachineDiagnosticAgent> logger)
    {
        _aiAgent=agent;
        _logger= logger;
        ragClinet=client;
    }

    public async Task<DiagnosticResponse> DiagnoseAsync(
        string machineId,
        string observedCondition,
        CancellationToken cancellationToken
    )
    {
        var ragResult = ragClinet.AskAsync(
             $"Investigate this machine condition: {observedCondition}",
             machineId,
             cancellationToken
        );

        var evidences=  $"""
                Retrieved knowledge from manufacturing documents:
                RAG Answer:
                {ragResult.Result.Answer}
                Supporting Sources:
                {string.Join("\n", ragResult.Result.Sources.Select(s =>
            $"- Document: {s.DocumentId}, File: {s.Filename}, Chunk: {s.ChunkId}, Distance: {s.Distance:F4}"))}
        """;


        var prompt = $"""
            Investigate the following manufacturing machine condition.

            Machine ID:{machineId}
            Observed condition:
            {observedCondition}
            {evidences}
            Provide a preliminary diagnostic assessment.

            Structure your response into:

            1. Observed facts
            2. Potential causes
            3. Recommended inspection steps
            4. Safety considerations
            5. Additional information required

            Important:
            - Clearly distinguish facts from hypotheses.
            - Do not invent machine history or manufacturer limits.
            - Do not present assumptions as confirmed diagnoses.
            - Never recommend bypassing safety interlocks.
            - Do not issue machine control commands.
            - Recommend qualified technician involvement where needed.
            """;

            var result =  await _aiAgent.RunAsync(prompt,cancellationToken:cancellationToken);

            _logger.LogInformation(
                 "Diagnostic completed for machine {MachineId}",
            machineId
            );
            return new DiagnosticResponse(
                machineId,
                result.Text,
                "Preliminary",
                 DateTimeOffset.UtcNow,
                ragResult.Result.Sources
            );
            
    }

} 