from websocket_app.app.app import App
from websocket_app.sockets import message

if __name__ == '__main__':
    try:
        # box = []
        # robot = []
        # for socket in message:
        #     if socket["act"].split('.')[0] == "robot":
        #         box.append(socket)
        App.app_box(message)
    except Exception as e:
        print("Error: %s" % e)
