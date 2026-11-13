from pydantic import BaseModel, Field

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



