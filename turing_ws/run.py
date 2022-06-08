import websockets
import asyncio
import json
import time


def ws_connect(messages, login_cookie):
    try:
        asyncio.get_event_loop().run_until_complete(_app_connect(messages, login_cookie))
    except Exception as e:
        print("Error: %s" % e)


async def _app_connect(messages, cookie):
    paths = 'ws://dev.turing-ws.com:8081/app/'
    async with websockets.connect(paths, extra_headers=cookie) as websocket:
        i = 0
        while 1:
            # This works fine - sends a message
            print("sending...")
            msg = json.dumps(messages).encode('utf-8')
            await websocket.send(msg)
            print("> {}".format(messages))
            try:
                print("receiving...")
                # This is the line that causes sadness
                data = await websocket.recv()
                print("< {}".format(data))
            except:
                # This doesn't happen either
                print("Listener is dead")
            i += 1
            time.sleep(5)
            if i == 3:
                break


if __name__ == '__main__':
    message = {
        "id": "abc",
        "act": "robot.relocalize",
        "arg": {"robot_id": "robot_test_10001", "scanning": "false",
                "pose": {"x": 2.430016077120822, "y": 1.555321336760925, "theta": -1.605265427794405}}
    }
    mes = {'s':'sss'}
    token_header = {
        'Cookie': "jwt=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTQyMjUzNjEsIm9yaWdfaWF0IjoxNjEzNjIwNTYxLCJyb2xlIjoiY3VzdG9tZXIiLCJ1c2VyX2lkIjo1MCwidXNlcm5hbWUiOiJ3YW5kYUB0dXJpbmd2aWRlby5uZXQiLCJ1dWlkIjoiMjFiOTU3NjctM2NlYy00YTc1LWI0YjctZjQ3MzE2ODA5OGQwIn0.Ul4quxBIq2-mW_8vhIIVWr0NJ-kMCXiR-X7lhqwMJg2rgVy3EQ9tKWTQJFMh3gMYmfTM07LRnzsRoIAuCX8dZg;path=/;domain=.turing-ws.com;haha=123"}

    ws_connect(message, token_header)
    ws_connect(mes, token_header)
