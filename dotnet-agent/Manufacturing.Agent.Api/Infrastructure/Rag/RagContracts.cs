using System.Text.Json.Serialization;

namespace Manufacturing.Agent.Api.Infrastructure.Rag;

public sealed record RagQueryRequest
{
    [JsonPropertyName("question")]
    public string Question { get; init; } = string.Empty;

    [JsonPropertyName("machine_id")]
    public string MachineId { get; init; } = string.Empty;
}

public sealed record RagQueryResponse
{
    [JsonPropertyName("question")]
    public string Question { get; init; } = string.Empty;

    [JsonPropertyName("answer")]
    public string Answer { get; init; } = string.Empty;

    [JsonPropertyName("sources")]
    public List<RagSource> Sources { get; init; } = [];
}

public sealed record RagSource
{
    [JsonPropertyName("document_id")]
    public string DocumentId { get; init; } = string.Empty;

    [JsonPropertyName("filename")]
    public string Filename { get; init; } = string.Empty;

    [JsonPropertyName("chunk_id")]
    public string ChunkId { get; init; } = string.Empty;

    [JsonPropertyName("distance")]
    public double Distance { get; init; }
}


