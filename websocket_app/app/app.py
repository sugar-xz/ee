from websocket_app.agent.connect_service import ConnectService
from websocket_app.agent.auth_service import AuthService
from websocket_app.agent.box_service import BoxService


class App:
    @classmethod
    def app_box(cls, message):
        cookie = AuthService.auth_system()

        # box_json, cookie = AuthService.box_initiate()
        # challenge = BoxService.box_initiate(box_json)
        # AuthService.box_authenticate(challenge)

        ConnectService.ws_connect(message, cookie)


if __name__ == '__main__':
    req1 = [        {
        "id": "abc",
        "act": "robot.relocalize",
        "arg": {"robot_id": "robot_test_10001", "scanning": "false", "pose": { "x": 2.430016077120822, "y": 1.555321336760925, "theta": -1.605265427794405}}
    }]
    App.app_box(req1)
