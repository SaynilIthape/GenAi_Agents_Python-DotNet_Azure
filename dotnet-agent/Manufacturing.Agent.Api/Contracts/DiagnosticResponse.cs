using Manufacturing.Agent.Api.Infrastructure.Rag;

namespace Manufacturing.Agent.Api.Contracts;

public sealed record DiagnosticResponse(
     string MachineId,
     string Assessment,
     string AssessmentStatus,
     DateTimeOffset GeneratedAtUtc,
     List<RagSource> Sources

);