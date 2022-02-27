from pydantic import BaseModel, constr


class ChatCreateRequest(BaseModel):
    chat_name: constr(max_length=255)
