from pydantic import BaseModel, Field
from typing import Optional

class ConversationCreate(BaseModel):
    title:str = Field(
        min_length=1,
        max_length=50
    )

class ConversationCreate(BaseModel):
    title:str = Field(
        min_length=1,
        max_length=50
    )

# For PUT: Requires all editable fields
class ConversationPut(BaseModel):
    title:str = Field(
        min_length=1,
        max_length=50
    )

# For PATCH: Every field is optional (defaults to None)
class ConversationPatch(BaseModel):
    title: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50
    )

