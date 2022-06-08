import requests
from websocket_app.config import config
from websocket_app.utils.utils import Utils


class AuthService:
    headers = {'X-APP': 'Box/%s/%s' % (config.BOX_LEVEL, config.BOX_VERSION), 'Content-Type': 'application/json'}

    @classmethod
    def auth_system(cls):
        url = config.HTTP_PATH + '/api/v1/user/auth/login'
        json = {"username": config.USERNAME, "password": config.PASSWORD}
        res = AuthService.post(url, json)

        res_cookies = requests.utils.dict_from_cookiejar(res.cookies)
        cookies = Utils.get_cookie(res_cookies)
        cookie = {'Cookie': cookies}
        # print("Add cookie: %s" % Cookie)
        return cookie

    @classmethod
    def box_initiate(cls):
        url = config.HTTP_PATH + '/api/v1/box/boxes/initiate'
        json = {"id": config.BOX_ID}
        res = AuthService.post(url, json)

        res_cookies = requests.utils.dict_from_cookiejar(res.cookies)
        cookies = Utils.get_cookie(res_cookies)
        cls.headers["Cookie"] = cookies
        cookie = {'Cookie': cookies}

        return res, cookie

    @classmethod
    def box_authenticate(cls, challenge):
        url = config.HTTP_PATH + '/api/v1/box/boxes/authenticate'
        json = {"type": config.BOX_TYPE,
                "challenge": challenge,
                "ip_address": "192.168.1.85"}
        res = AuthService.post(url, json)

        print(res.json())
        return res

    @classmethod
    def post(cls, url, json, **kwargs):
        try:
            s = requests.session()
            s.headers.update(cls.headers)
            res = s.post(url, json=json)
            return res
        except:
            print("Fail port request!!")
