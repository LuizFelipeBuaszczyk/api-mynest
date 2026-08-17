from pydantic import BaseModel

class RequestPostPassword(BaseModel):
    name: str
    description: str | None=None
    password: str

class ResponsePostPassword(BaseModel):
    message: str="Password registered"

class ResponseListPasswordObject(BaseModel):
    id: int
    name: str

class ResponseListPassword(BaseModel):
    data: list[ResponseListPasswordObject]

class ResponseGetPassword(BaseModel):
    id: int
    password: str
    name: str
    description: str | None=None

class ResponseDeletePassword(BaseModel):
    message: str="Password deleted"
