import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    input = context.get_input()
    result = yield context.call_activity("azfn_task", input["request_id"])
    return result


main = df.Orchestrator.create(orchestrator_function)
