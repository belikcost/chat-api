from pydantic import BaseModel


class SendChatMessageRequest(BaseModel):
    chat_id: str
    user_id: str
    message: str