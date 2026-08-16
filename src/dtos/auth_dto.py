from pydantic import BaseModel

class PostAuthLoginDTO(BaseModel):
    username: str
    password: str

class ResponsePostAuthLoginDTO(BaseModel):
    access_token: str
    refresh_token: str

class PostAuthRefreshTokenDTO(BaseModel):
    refresh_token: str

class ResponsePostAuthRefreshTokenDTO(BaseModel):
    access_token: str
