from typing import List

from pydantic import BaseModel


class GetChatMessagesRequest(BaseModel):
    chat_id: str
    limit: int
    from_cursor: List[str] = []
