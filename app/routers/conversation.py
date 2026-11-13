
from fastapi import APIRouter, HTTPException, status
from app.schemas.conversation import ConversationCreate

conversations = {}

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)

@router.get("")
def get_conversations():
    return {"conversations":list(conversations.values())}

@router.post("")
def create_conversation(data:ConversationCreate):
    conversation_id = len(conversations) + 1
    conversation = {
        "id": conversation_id,
        "title": data.title,
        "messages": []
    }

    conversations[conversation_id] = conversation
    return conversation

@router.put("/{conversation_id}")
def replace_conversations(conversation_id:int, data:ConversationCreate):
    if conversation_id not in conversations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found"
        )

    conversations[conversation_id]["title"] = data.title
    return {"conversations":conversation_id, "message": "replaced"}

@router.patch("/{conversation_id}")
def replace_conversations(conversation_id:int, data:ConversationCreate):
    if conversation_id not in conversations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found"
        )

    # Extract only the fields the user actually sent in the request
    conversations[conversation_id] = data.model_dump(exclude_unset=True)
    return {"conversations":conversation_id, "message": "partially updated"}

@router.delete("/{conversation_id}")
def delete_conversations(conversation_id:int):
    if conversation_id not in conversations:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Converation not found"
        )

    del conversations[conversation_id]
    return {"conversations":conversation_id, "message": "deleted"}
