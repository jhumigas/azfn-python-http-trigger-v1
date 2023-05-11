from uuid import uuid1

import azure.durable_functions as df
import azure.functions as func

from py_project.logger import logger


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    func_name = "azfn_orchestrator"
    client = df.DurableOrchestrationClient(starter)
    request_id = str(uuid1())
    instance_id = await client.start_new(
        orchestration_function_name=func_name,
        client_input={
            "request_id": request_id,
        },
        instance_id=None,
    )
    logger.info((f"Started orchestration with ID = {instance_id}" f"-- func_name = {func_name}"))

    return client.create_check_status_response(req, instance_id)
