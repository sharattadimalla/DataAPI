import uuid


def generate_guid() -> str:
    return str(uuid.uuid4())
