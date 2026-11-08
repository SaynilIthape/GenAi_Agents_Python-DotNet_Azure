namespace Manufacturing.Agent.Api.Contracts;

public sealed record DiagnosticRequest(
    string? MachineId,
    string? ObservedCondition
);