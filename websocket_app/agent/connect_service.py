import websockets
import asyncio
from websocket_app.agent.ws_service import WebSocketService
from websocket_app.config.config import WS_PATH


class ConnectService(object):

    @classmethod
    def ws_connect(cls, message, login_cookie):
        try:
            asyncio.get_event_loop().run_until_complete(ConnectService._app_connect(message, login_cookie))
        except Exception as e:
            print("Error: %s" % e)

    @classmethod
    async def _app_connect(cls, message, cookie):
        paths = WS_PATH + '/channel/app'
        async with websockets.connect(paths, extra_headers=cookie) as websocket:
            conn = WebSocketService(websocket)
            for item in message:
                await conn.s_send(item)
                await conn.s_recv()
