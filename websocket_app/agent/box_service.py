import json
from websocket_app.agent import BASE_DIR
from websocket_app.utils.utils import Utils


class BoxService:
    @classmethod
    def box_initiate(cls, response, **extra_kwargs):
        strJson = BoxService._validate_pro_key("box_key")
        private_key = strJson['private_key'].encode()

        challenge = response.json()['ret']['challenge']
        challenge = Utils.a2b_base64(challenge)
        challenge = Utils.pem_decrypt(challenge, private_key, False)
        challenges = Utils.b2a_base64(challenge)

        return challenges

    @classmethod
    def _validate_pro_key(cls, pro, **extra_kwargs):
        data = open(BASE_DIR + "/config/" + pro + ".json", encoding='utf-8')
        # 转换为python对象
        strJson = json.load(data)
        return strJson
