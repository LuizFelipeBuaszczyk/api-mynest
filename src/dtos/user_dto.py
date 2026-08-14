from pydantic import BaseModel
from typing import Optional

class PostUserDTO(BaseModel):
    username: str
    password: str
    email: Optional[str]=None
