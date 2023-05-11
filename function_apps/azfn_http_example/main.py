from py_project.logger import logger
import azure.functions as func
from py_project import __version__


def main(req: func.HttpRequest) -> func.HttpResponse:
    logger.info("Python HTTP trigger function processed a request.")

    return func.HttpResponse(f"{__version__}")


if __name__ == "__main__":
    main(None)
