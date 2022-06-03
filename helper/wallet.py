# -*- coding: utf-8 -*-

# File: wallet.py

"""
   Description: 
        -
        -
"""
import requests
from web3 import Web3, HTTPProvider
from eth_account import Account
from eth_account.messages import defunct_hash_message
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account.messages import encode_defunct


class Wallet(object):

    def __init__(self, public_address: str, private_key: str, host: str):
        self.private_key = private_key
        self.public_address = public_address
        self.account = Account.from_key(private_key)

        self.web3 = Web3(HTTPProvider(public_address))
        self.web3.middleware_onion.add(
            construct_sign_and_send_raw_middleware(self.account)
        )
        self.web3.eth.default_account = self.account.address
        self.host = host
        self.headers = {}

    def sign_msg(self, msg):
        _message = encode_defunct(text=msg)
        return self.web3.eth.account.sign_message(_message, self.private_key).signature.hex()

    def set_headers(self, headers):
        self.headers = headers

    def open(self, *args, **kwargs):
        _url = args[0] or kwargs['url']
        _url = f'{self.host}{_url}' if 'http' not in _url else _url
        response = requests.request(
            **kwargs,
            headers=self.headers,
            url=_url
        )
        return response

    def get(self, *args, **kw):
        """Like open but method is enforced to GET."""
        kw["method"] = "GET"
        return self.open(*args, **kw)

    def patch(self, *args, **kw):
        """Like open but method is enforced to PATCH."""
        kw["method"] = "PATCH"
        return self.open(*args, **kw)

    def post(self, *args, **kw):
        """Like open but method is enforced to POST."""
        kw["method"] = "POST"
        return self.open(*args, **kw)

    def head(self, *args, **kw):
        """Like open but method is enforced to HEAD."""
        kw["method"] = "HEAD"
        return self.open(*args, **kw)

    def put(self, *args, **kw):
        """Like open but method is enforced to PUT."""
        kw["method"] = "PUT"
        return self.open(*args, **kw)

    def delete(self, *args, **kw):
        """Like open but method is enforced to DELETE."""
        kw["method"] = "DELETE"
        return self.open(*args, **kw)

    def options(self, *args, **kw):
        """Like open but method is enforced to OPTIONS."""
        kw["method"] = "OPTIONS"
        return self.open(*args, **kw)

    def trace(self, *args, **kw):
        """Like open but method is enforced to TRACE."""
        kw["method"] = "TRACE"
        return self.open(*args, **kw)
