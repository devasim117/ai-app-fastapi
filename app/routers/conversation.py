
from fastapi import APIRouter
from app.schemas.conversation import ConversationCreate

conversations = {}

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)

@router.post("")
def create_conversation(data:ConversationCreate):
    conversation_id = len(conversations) + 1
    conversation = {
        "id": conversation_id,
        "title": data.title,
        "messages": []
    }

    conversations[id] = conversation
    return conversation

