import azure.functions as func
import logging
from ADD import ADD

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.


@app.function_name(name="calculatorApp")
@app.route(route="add")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
     logging.info('Python HTTP trigger function processed a request.')

     val1 = req.params.get('val1')
     val2 = req.params.get('val2')
     summ = ADD().addition(val1, val2)

    return func.HttpResponse(f"Hello, {summ}. This HTTP triggered function executed successfully.")
    