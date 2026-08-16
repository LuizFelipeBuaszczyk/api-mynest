from pydantic import BaseModel


class RequestPostPassword(BaseModel):
    password: str

class ResponsePostPassword(BaseModel):
    message: str="Password registered"

class ResponseListPasswordObject(BaseModel):
    id: int

class ResponseListPassword(BaseModel):
    data: list[ResponseListPasswordObject]

class ResponseGetPassword(BaseModel):
    id: int
    password: str

class ResponseDeletePassword(BaseModel):
    message: str="Password deleted"
