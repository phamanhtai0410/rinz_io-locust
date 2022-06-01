# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import hashlib
import hmac
import json

secret_key = 'WH5syh7jdcftvJNaUEsU38RymzRkjLp2'
api_key = 'MTTWPQuj3jmebr2RYyq4UWQZx8qxKsJn'


def sha512(data, secret_key):
    _key = str(secret_key).encode('utf-8')
    byte_input = data.encode('utf-8')
    return hmac.new(_key, byte_input, hashlib.sha512).hexdigest()


def print_done(msg: str):
    print(f'\033[92m [✔ DONE] {msg}  \033[0m')


def sign_data(body: dict):
    _check_data = sorted(body.items())
    _string = json.dumps(_check_data)
    _hash_value = sha512(_string, secret_key)
    return {
               **body,
               'code': _hash_value
           }, api_key
