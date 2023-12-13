import uuid
import redis
from models import UserInput


def generate_guid() -> str:
    return str(uuid.uuid4()).replace("-", "")


def get_redis_conn():
    r = redis.Redis(host="redis_service", port=6379, db=0)
    return r


def generate_sql(input: UserInput):
    TBL_NM = UserInput.entity_name
    KEY = UserInput.key
    VALUE = UserInput.value
    START_DT = UserInput.start_date
    END_DT = UserInput.end_data
    SQL_CMD = f"SELECT * FROM {TBL_NM} WHERE {KEY} = {VALUE} AND \
                LOAD_DATE BETWEEN {START_DT} AND {END_DT}"
    return SQL_CMD
