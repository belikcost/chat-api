from pydantic import BaseModel, constr


class JoinChatUserRequest(BaseModel):
    chat_id: str
    user_name: constr(max_length=255)
