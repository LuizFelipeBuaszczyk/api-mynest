from pydantic import BaseModel

class RequestPostRoles(BaseModel):
    codename: str
    description: str | None = None

class ResponsePostRoles(BaseModel):
    message: str = "Role registered"

class ResponseListRoleObject(BaseModel):
    id: int
    codename: str

class ResponseListRoles(BaseModel):
    data: list[ResponseListRoleObject]

class ResponseGetRole(BaseModel):
    id: int
    codename: str
    description: str | None = None