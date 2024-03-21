import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    bot_token: str
    chat_id: str
    message: str


@app.post("/send_message")
async def send_message(message: Message):
    bot_token = message.bot_token
    chat_id = message.chat_id
    message_text = message.message

    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message_text
    }

    response = requests.post(telegram_url, json=payload)

    if response.ok:
        return {"status": "success", "message": "Message sent successfully"}
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to send message")
