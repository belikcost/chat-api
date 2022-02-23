from aiohttp import web
from pydantic import ValidationError

from src.components.schemas.GetChatMessagesRequest import GetChatMessagesRequest


async def get_chat_messages(request: web.Request):
    chat_id = request.match_info["chat_id"]
    query_params = {**request.query}

    if "from" in query_params:
        query_params["from_cursor"] = query_params["from"].replace("[", "").replace("]", "").split(",")

    try:
        request_data = GetChatMessagesRequest(**query_params, chat_id=chat_id)
    except ValidationError as e:
        return web.json_response(status=400, data=e.errors())

    if str(chat_id) == "123":
        return web.json_response(status=404, data={"message": "Указанный чат не существует"})

    if not 1 <= request_data.limit <= 1000:
        return web.json_response(status=400, data={"message": "1 <= limit <= 1000"})

    return web.json_response(data=[{"id": 123}])
