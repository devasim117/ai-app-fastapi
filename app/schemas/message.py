from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=2000,
        description="Message sent by user"
    )

    model: str = Field(
        default="phi",
        description="AI model identifier"
    )

class ChatResponse(BaseModel):
    message:str
    model:str
    response:str