from pydantic import BaseModel

class PostAuthLoginDTO(BaseModel):
    username: str
    password: str
