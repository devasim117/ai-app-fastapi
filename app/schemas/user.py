from pydantic import BaseModel, Field
from typing import List

class UserRequest(BaseModel):
    email: str = Field(
        min_length=5,
        max_length=50,
        description="user email"
    )
    password:str = Field(
        min_length=6,
        max_length=20,

        description="message set by user"
    )

class UserResponse(BaseModel):
    id: int 
    email: str

class UserList(BaseModel):
    users:List[UserResponse]