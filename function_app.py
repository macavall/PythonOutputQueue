import azure.functions as func
import logging
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueClient

# Use DefaultAzureCredential to authenticate via managed identity
credential = DefaultAzureCredential()

# Initialize the QueueClient statically using managed identity
queue_client = QueueClient(
    account_url="https://pythonlog5611stor.queue.core.windows.net/",
    queue_name="queue1",
    credential=credential
)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http1")
def http1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    queue_message = f"Hello there! Message from HTTP triggered function."
    queue_client.send_message(queue_message)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

# ========================================================================
# ========================================================================

@app.route(route="http2", auth_level=func.AuthLevel.ANONYMOUS)
def http2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    queue_message = f"Hello there! Message from HTTP triggered function."
    queue_client.send_message(queue_message)

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )