from pydantic import BaseModel

class requestUserLoginDTO(BaseModel):
    username: str
    password: str

class requestUserRegisterDTO(BaseModel):
    username: str
    password: str