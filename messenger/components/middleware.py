from typing import Callable, Awaitable

from aiohttp import web


@web.middleware
async def middleware(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.Response]]
):
    try:
        if not request.method == "POST":
            return await handler(request)

        if not request.body_exists:
            return web.json_response(status=400, data={"message": "Request body required!"})
        else:
            return await handler(request)
    except Exception as ex:
        return web.json_response(status=400, data={"message": str(ex)})

