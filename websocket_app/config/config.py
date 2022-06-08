# uri username password
WHERE = 'local'

if WHERE == 'local':
    HTTP_PATH = 'http://local-test.turingvideo.cn:8000'
    BOX_TYPE = 'std_sr_v1'
    BOX_LEVEL = 1
    WS_PATH = 'ws://local-test.turingvideo.cn:8081'  # websocket
else:
    HTTP_PATH = 'https://dev-api.turingvideo.cn'
    BOX_TYPE = 'dog_sr_v1'
    BOX_LEVEL = 0
    WS_PATH = 'wss://dev-ws.turingvideo.cn:8443'  # websocket

USERNAME = "customer@turingvideo.net"
PASSWORD = "1234qwer"

BOX_ID = "box_dog_sr_50006"
BOX_VERSION = '1.0.0'
