from aiohttp import web
from pydantic import ValidationError

from src.components.schemas.SendChatMessageRequest import SendChatMessageRequest


async def send_chat_message(request: web.Request):
    chat_id = request.match_info["chat_id"]
    request_body = await request.json()

    try:
        request_data = SendChatMessageRequest(**request_body, **request.query, chat_id=chat_id)
    except ValidationError as e:
        return web.json_response(status=400, data=e.errors())

    if str(chat_id) == "123":
        return web.json_response(status=404, data={"message": "Указанный чат не существует"})

    if str(request_data.user_id) == "123":
        return web.json_response(status=404, data={"message": "Указанного пользователя нет в чате"})

    return web.json_response(data=[{"id": 123}])