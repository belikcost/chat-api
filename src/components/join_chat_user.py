from aiohttp import web
from pydantic import ValidationError

from src.components.schemas.JoinChatUserRequest import JoinChatUserRequest


async def join_chat_user(request):
    chat_id = request.match_info["chat_id"]
    request_body = await request.json()

    try:
        JoinChatUserRequest(**request_body, chat_id=chat_id)
    except ValidationError as e:
        return web.json_response(status=400, data=e.errors())

    if str(chat_id) == "123":
        return web.json_response(status=404, data={"message": "Указанный чат не существует"})

    return web.json_response(status=201, data={"user_id": "123"})
