import websockets
import asyncio
import json
import requests


def auth_token():
    url = 'https://dev-gw.turingvideo.cn/auth/'
    headers = {'X-APP': 'Box/1/1.0.0', 'Content-Type': 'application/json'}
    u_p = {"username": "dev@turingvideo.net", "password": "$Turin9Vide0"}
    s = requests.session()
    s.headers.update(headers)
    res = s.post(url, json=u_p)
    res_cookies = requests.utils.dict_from_cookiejar(res.cookies)
    cookies = get_cookie(res_cookies)
    cookie = {'Cookie': cookies}
    return cookie


def get_cookie(cookies):
    cookie = ''
    if len(cookies) > 0:
        cookie = _cookies_to_string(cookies)
    return cookie


def _cookies_to_string(cookies):
    string = []
    for k, v in cookies.items():
        string.append('%s=%s' % (k, v))
    string = ';'.join(string)
    return string


def ws_connect(messages, login_cookie):
    try:
        asyncio.get_event_loop().run_until_complete(_app_connect(messages, login_cookie))
    except Exception as e:
        print("Error: %s" % e)


async def _app_connect(messages, cookie):
    paths = 'wss://dev-ws.turingvideo.cn:8443/channel/app'
    async with websockets.connect(paths, extra_headers=cookie) as websocket:
        # This works fine - sends a message
        print("sending...")
        await websocket.send(json.dumps(messages))
        print("> {}".format(messages))
        try:
            print("receiving...")
            # This is the line that causes sadness
            data = await websocket.recv()
            print("< {}".format(data))
        except:
            # This doesn't happen either
            print("Listener is dead")


if __name__ == '__main__':
    message = {
        "id": "abc",
        "act": "box.debug_echo",
        "arg": {"box_id": "box_dog_sr_50006"}
    }
    token_header = auth_token()
    ws_connect(message, token_header)
