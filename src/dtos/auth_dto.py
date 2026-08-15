from pydantic import BaseModel

class PostAuthLoginDTO(BaseModel):
    username: str
    password: str

class ResponsePostAuthLoginDTO(BaseModel):
    access_token: str
    refresh_token: str
