from fastapi import APIRouter
from app.schemas.user import UserRequest,UserResponse,UserList

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = []

@router.post("/")
def create_user(request: UserRequest):
    user_id = len(users) + 1
    user = {
        "id": user_id,
        "email": request.email,
        "password": request.password
    }

    users.append(user)
    return {"user":UserResponse(id=user_id,email=request.email)}

@router.get("/")
def get_users():
    return UserList(users=users)
    