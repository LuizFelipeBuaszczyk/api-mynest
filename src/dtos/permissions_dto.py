from pydantic import BaseModel

class ResponseListPermissionObject(BaseModel):
    id: int
    codename: str
    description: str | None = None

class ResponseListPermissions(BaseModel):
    data: list[ResponseListPermissionObject]