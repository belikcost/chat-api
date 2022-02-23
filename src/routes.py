from aiohttp import web

from src.components.send_chat_message import send_chat_message
from src.components.get_chat_messages import get_chat_messages
from src.components.join_chat_user import join_chat_user
from src.components.create_chat import create_chat


def setup_routes(app, base_path="/"):
    app.add_routes([
        web.post(base_path + "/chats", create_chat),
        web.post(base_path + "/chats/{chat_id}/users", join_chat_user),
        web.get(base_path + "/chats/{chat_id}/messages", get_chat_messages),
        web.post(base_path + "/chats/{chat_id}/messages", send_chat_message)
    ])
