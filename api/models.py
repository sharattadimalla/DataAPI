from pydantic import BaseModel
from typing import List


class UserInput(BaseModel):
    entity_name: str
    key: str
    value: str
    start_date: str = None
    end_data: str = None


class UserResponse(BaseModel):
    request_id: str
    status: str
    data: List[dict] = None
