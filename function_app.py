import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Default template function (KEEP IT AS IS)
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get('name')
        except:
            name = None

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully.",
            status_code=200
        )


# --------------------------------------------------------------
# SIMPLE JSON VALIDATION FUNCTION (YOUR MAIN TASK)
# --------------------------------------------------------------
@app.route(route="validate")
def validate(req: func.HttpRequest) -> func.HttpResponse:
    
    # Try to read JSON body
    try:
        data = req.get_json()
    except:
        return func.HttpResponse(
            json.dumps({
                "isValid": False,
                "errors": ["Invalid JSON format"]
            }),
            mimetype="application/json"
        )

    errors = []

    # Required fields check
    for field in ["name", "age", "email"]:
        if field not in data:
            errors.append(f"Missing field: {field}")

    # Age check
    if "age" in data:
        age = data["age"]
        if not isinstance(age, (int, float)):
            errors.append("Age must be a number")
        elif age <= 0:
            errors.append("Age must be greater than 0")

    # Email check
    if "email" in data:
        email = data["email"]
        if "@" not in str(email):
            errors.append("Email must contain '@'")

    # Final result
    result = {
        "isValid": len(errors) == 0,
        "errors": errors
    }

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json"
    )
