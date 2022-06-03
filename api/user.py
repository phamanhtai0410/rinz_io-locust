# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from locust import HttpUser, constant_throughput
from pydash import get

from helper.wallet import Wallet
import json

with open("../fake_account.json") as f:
    accounts = json.load(f)


class IdService(HttpUser):
    wait_time = constant_throughput(1)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.wallet = None

    def on_start(self):
        """
        - Login
        :return:
        """
        _account = accounts.pop()
        self.wallet = Wallet(
            public_address=get(_account, 'public_address'),
            private_key=get(_account, 'private_key'),
            host=''
        )

        obj = self.client.get('/v1/user/auth/validate', params={
            'public_address': self.wallet.public_address
        })
        print(obj)
        assert obj, 'Get message fail'
        _json = obj.json()

        _msg = get(_json, 'data.message')
        assert _msg, "Message is None"
        _signature = wallet.sign_msg(_msg)
        _nonce = pydash.get(_json, 'data.nonce')
        print(_signature)

        _res = self.client.post("/v1/user/auth/login", json={
            "publicAddress": wallet.public_address,
            "signature": _signature,
            "nonce": _nonce
        }, headers={'content-type': 'application/json'})
        _json = _res.json()
        print('_json', _json)
        _access_token = pydash.get(_json, 'data.accessToken', default=None)
        print(_access_token)
        assert _access_token, 'Get token fail'
        self.client.headers = {
            'Authorization': f'Bearer {_access_token}'
        }
