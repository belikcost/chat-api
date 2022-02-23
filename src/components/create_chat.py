from aiohttp import web
from pydantic import ValidationError

from src.components.schemas.ChatCreateRequest import ChatCreateRequest


async def create_chat(request):
    request_body = await request.json()

    try:
        ChatCreateRequest(**request_body)
    except ValidationError as e:
        return web.json_response(status=400, data=e.errors())

    response_body = {"chat_id": 123}
    return web.json_response(status=201, data=response_body, content_type="application/json")
