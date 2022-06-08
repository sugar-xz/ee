import binascii
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend


class Utils:
    @classmethod
    def get_cookie(cls, cookies):
        cookie = ''
        if len(cookies) > 0:
            cookie = Utils._cookies_to_string(cookies)
        return cookie

    @classmethod
    def _cookies_to_string(cls, cookies):
        string = []
        for k, v in cookies.items():
            string.append('%s=%s' % (k, v))
        string = ';'.join(string)
        return string

    @classmethod
    def pem_decrypt(cls, cipher_text, pem_private_key, sha1=False):
        pad = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA512()), algorithm=hashes.SHA512(), label=None)
        sha1_pad = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA1()), algorithm=hashes.SHA1(), label=None)
        if sha1:
            pads = sha1_pad
        else:
            pads = pad
        private_key = serialization.load_pem_private_key(pem_private_key, None, default_backend())
        plain_text = private_key.decrypt(cipher_text, pads)
        return plain_text

    @classmethod
    def b2a_base64(cls, data):
        data = binascii.b2a_base64(data)[:-1]
        data = data.decode('ascii')
        return data

    @classmethod
    def a2b_base64(cls, data):
        data = data.encode('ascii')
        data = binascii.a2b_base64(data)
        return data