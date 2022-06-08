from box import Box
import binascii
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def get_token(response, **extra_kwargs):
    return Box({"get_csrftoken": response.cookies['csrftoken'], "get_login_id": response.json()['ret']['id']})

def validate_err_200(response, **extra_kwargs):
    _validate_no_err(response)

def validate_err_201(response, **extra_kwargs):
    _validate_no_err(response)

def validate_err_400(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 103
    assert err_info['em'] == "Please submit a valid input. (input)"
    assert err_info['dm'] == "input"

def validate_err_401(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 104
    assert err_info['em'] == "Please sign in. (not_in)"
    assert err_info['dm'] == "not_in"
    extra_info = response.json()['extra']
    assert 'detail' in extra_info
    # assert extra_info['detail'] == "Authentication credentials were not provided."

def validate_err_403(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 105
    assert err_info['em'] == "This operation is forbidden. (forbidden)"
    assert err_info['dm'] == "forbidden"
    extra_info = response.json()['extra']
    assert 'detail' in extra_info

def validate_err_404(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 106
    assert err_info['em'] == "This instance doesn't exist any more. (none)"
    assert err_info['dm'] == "none"


def validate_err_405(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 102
    assert err_info['em'] == "Please use a valid method. (method)"
    assert err_info['dm'] == "method"

def validate_err_406(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 101
    assert err_info['em'] == "Your app is outdated. Please update it now. (agent)"
    assert err_info['dm'] == "agent"

def validate_err_409(response, **extra_kwargs):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    # assert err_info['ec'] == 106
    # assert err_info['em'] == "Invalid email or password. (none)"
    # assert err_info['dm'] == "none"
    # assert err_info['ec'] == 107
    # assert err_info['em'] == "You have no permission. (permission)"
    # assert err_info['dm'] == "permission"

def validate_camera_create(response, **extra_kwargs):
    _validate_no_err(response)
    data = response.json()['ret']
    assert 'created' in data
    assert 'updated' in data

def validate_camera_create_get_params(response, **extra_kwargs):
    params = []
    params.append(response.json()['ret']['cameras'][0]['id'])
    params.append(response.json()['ret']['cameras'][0]['mac_address'])
    params.append(response.json()['ret']['cameras'][0]['rules'][0]['id'])
    getParam = ['get_camera_id','get_mac_address','get_rules_id']
    return Box({getParam[0]: params[0], getParam[1]: params[1], getParam[2]: params[2]})

def validate_camera_delete(response, **extra_kwargs):
    _validate_no_err(response)
    data = response.json()['ret']
    assert 'deleting' in data
    assert 'increased' in data

def validate_box_initiate_get_challenge(response, **extra_kwargs):
    strJson = _validate_pro_key("box_key")
    private_key = strJson['private_key'].encode()

    challenge = response.json()['ret']['challenge']
    challenge = _a2b_base64(challenge)
    challenge = _pem_decrypt(challenge, private_key, False)
    challenge = _b2a_base64(challenge)

    return Box({"get_box_challenge": challenge})

def validate_robot_initiate_get_challenge(response, **extra_kwargs):
    strJson = _validate_pro_key("robot_key")
    private_key = strJson['private_key'].encode()

    challenge = response.json()['ret']['challenge']
    challenge = _a2b_base64(challenge)
    challenge = _pem_decrypt(challenge, private_key, False)
    challenge = _b2a_base64(challenge)

    return Box({"get_robot_challenge": challenge})

def validate_box_claim(**extra_kwargs):
    strJson = _validate_pro_key("box_key")
    json = {
        "id": strJson['id'],
        "signature": strJson['signature']
    }
    return Box(json)

def validate_camera_cameras(response, **extra_kwargs):
    data = response.json()['ret']['results'][0]['id']
    return Box({"get_camera_cameras_id": data})

def validate_user_add_cameras(response, **extra_kwargs):
    data = response.json()['ret']['id']
    return Box({"get_user_add_cameras_id": data})

def validate_get_domain_type_parent_id(response, **extra_kwargs):
    _validate_no_err(response)
    data = response.json()['ret']
    assert 'id' in data
    parent_id = response.json()['ret']['id']
    return Box({"domain_type_parent_id": parent_id})

def validate_get_domain_parent_id(response, **extra_kwargs):
    _validate_no_err(response)
    data = response.json()['ret']
    assert 'id' in data
    parent_id = response.json()['ret']['id']
    return Box({"domain_parent_id": parent_id})

def validate_box_get_token(response, **extra_kwargs):
    _validate_no_err(response)
    data = response.json()['ret']
    assert 'url' in data
    assert 'fields' in data
    assert 'user_id' in data

def _validate_pro_key(pro, **extra_kwargs):
    import json
    from api_tests import TEST_BASE_DIR
    data = open(TEST_BASE_DIR + "/variables/" + pro + ".json", encoding='utf-8')
    # 转换为python对象
    strJson = json.load(data)
    return strJson

def _validate_no_err(response):
    err_info = response.json()['err']
    assert 'ec' in err_info
    assert 'em' in err_info
    assert 'dm' in err_info
    assert err_info['ec'] == 0
    assert err_info['em'] == "This operation is successful."
    assert err_info['dm'] == "ok"

def _pem_decrypt(cipher_text, pem_private_key, sha1=False):
    pad = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()), algorithm=hashes.SHA512(), label=None)
    sha1_pad = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()), algorithm=hashes.SHA1(), label=None)
    if sha1:
        pads = sha1_pad
    else:
        pads = pad
    private_key = serialization.load_pem_private_key(pem_private_key, None, default_backend())
    plain_text = private_key.decrypt(cipher_text, pads)
    return plain_text

def _b2a_base64(b):
    b = binascii.b2a_base64(b)[:-1]
    b = b.decode('ascii')
    return b

def _a2b_base64(b):
    b = b.encode('ascii')
    b = binascii.a2b_base64(b)
    return b
