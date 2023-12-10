from pydantic import BaseModel
from typing import List


class UserInput(BaseModel):
    entity_name: str
    start_date: str
    end_data: str


class UserResponse(BaseModel):
    request_id: str
    status: str
    data: List[dict]
