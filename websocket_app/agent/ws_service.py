import json


class WebSocketService:

    def __init__(self, websocket):
        self.websocket = websocket

    async def s_send(self, message):
        # This works fine - sends a message
        print("sending...")
        await self.websocket.send(json.dumps(message))
        print("> {}".format(message))

    async def s_recv(self):
        # This stops at the await and never receives
        try:
            print("receiving...")
            # This is the line that causes sadness
            data = await self.websocket.recv()
            print("< {}".format(data))
        except:
            # This doesn't happen either
            print("Listener is dead")
