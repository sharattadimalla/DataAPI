import json
import pickle
from fastapi import FastAPI, Request
from models import UserInput, UserResponse
from utils import generate_guid, get_redis_conn, generate_sql

app = FastAPI(
    title="Data API",
    summary="API to retrieve data",
    version="0.0.1",
    swagger_ui_parameters={"syntaxHighlight": False},
)

redis_conn = get_redis_conn()


@app.post("/data/share", status_code=201)
async def request_data(payload: UserInput) -> str:
    """POST /data endpoint to accept data requested by the user

    Returns:
        str: returns a request_id used to track data request
    """
    share_id = generate_guid()
    redis_conn.hmset(share_id, mapping=json.loads(payload.model_dump_json()))
    return share_id


@app.get("/data/share/{id}", status_code=200)
def get_data(id: str) -> UserResponse:
    """GET /data/{id} to retrieve data requested by the user

    Returns:
        json: returns a json object of items of class Item
    """
    resp = redis_conn.hgetall(id)
    return json.dumps(resp)


@app.put("/private/sql", status_code=200)
def get_sql_query(input: UserInput) -> str:
    """GET /private/sql to generate SQL query based on User Input

    Returns:
        str: returns a SQL query that can be executed on the warehouse
    """
    return generate_sql(input)
