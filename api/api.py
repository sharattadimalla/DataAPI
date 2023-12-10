from fastapi import FastAPI
from models import UserInput, UserResponse
from utils import generate_guid

app = FastAPI(
    title="Data API",
    summary="API to retrieve data",
    version="0.0.1",
    swagger_ui_parameters={"syntaxHighlight": False},
)


@app.post("/data", status_code=201)
def request_data(payload: UserInput) -> str:
    """POST /data endpoint to accept data requested by the user

    Returns:
        str: returns a request_id used to track data request
    """

    result = generate_guid()
    return result


@app.get("/data/{id}", status_code=200)
def get_data(id: str) -> UserResponse:
    """GET /data/{id} to retrieve data requested by the user

    Returns:
        json: returns a json object of items of class Item
    """

    resp = UserResponse(request_id=id, data=[])
    print(resp)
    return resp
