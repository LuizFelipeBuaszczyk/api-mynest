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

class RequestPostRolePermissions(BaseModel):
    permission_ids: list[int]

class ResponsePostRolePermissions(BaseModel):
    message: str = "Permissions assigned to role"