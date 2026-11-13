import asyncio
from fastapi import FastAPI
from app.schemas.message import ChatRequest,ChatResponse
from app.routers import users, conversation

app = FastAPI(
    title="AI backend api",
    description="Learning fast api for ai",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(conversation.router)

@app.get("/")
def home():
    return {"message":"Welcome to ai api","status":"running"}

@app.get("/health")
def health_check():
    return {"status":"healthy"}

@app.post("/chat")
async def chat(request:ChatRequest):
    ai_response = f"you said: {request.message}"
    await asyncio.sleep(2)
    return ChatResponse(message=request.message, model=request.model, response=ai_response )

