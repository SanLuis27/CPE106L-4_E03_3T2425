import json
import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')

def load_users():
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

# --- Models ---
class LoginRequest(BaseModel):
    username: str
    password: str

class NotificationRequest(BaseModel):
    user_id: str
    message: str

class MessageRequest(BaseModel):
    sender_id: str
    recipient_id: str
    content: str

# --- Endpoints ---
@router.post("/login")
def login(request: LoginRequest):
    users = load_users()
    for user in users:
        if user["username"] == request.username and user["password"] == request.password:
            return {"status": "success", "message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@router.post("/notify")
def send_notification(request: NotificationRequest):
    # Dummy notification logic
    return {"status": "sent", "user_id": request.user_id, "message": request.message}

@router.post("/message")
def send_message(request: MessageRequest):
    # Dummy messaging logic
    return {"status": "delivered", "from": request.sender_id, "to": request.recipient_id, "content": request.content}
