from fastapi import FastAPI
from api_controller import router as api_router

app = FastAPI()

@app.get("/login")
def login_get():
    return {"message": "Use POST with JSON body {username, password} to login."}

@app.get("/notify")
def notify_get():
    return {"message": "Use POST with JSON body {user_id, message} to send notification."}

@app.get("/message")
def message_get():
    return {"message": "Use POST with JSON body {sender_id, recipient_id, content} to send a message."}

# Custom root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the API! Use /docs for documentation."}

# Integrate APIController endpoints
app.include_router(api_router)
