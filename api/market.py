# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
# -*- coding: utf-8 -*-

from locust import HttpUser, constant_throughput, task
from pydash import get

from helper.wallet import Wallet
import json

# with open("fake_stag_accounts.json") as f:
#     accounts = json.load(f)


class MarketService(HttpUser):
    # wait_time = constant_throughput(1)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     _account = accounts.pop()
    #     print(_account)
    #     self.wallet = Wallet(
    #         public_address=get(_account, 'address'),
    #         private_key=get(_account, 'private_key'),
    #         host=''
    #     )
    #
    # def on_start(self):
    #     """
    #     - Login
    #     :return:
    #     """
    #
    #     obj = self.client.get('/v1/id/auth/message', params={
    #         'public_address': self.wallet.public_address
    #     })
    #     _json = obj.json()
    #
    #     _msg = get(_json, 'data.sign_msg')
    #     _signature = self.wallet.sign_msg(_msg)
    #     _nonce = get(_json, 'data.nonce')
    #     print(_signature)
    #
    #     _res = self.client.post("/v1/id/auth/login", json={
    #         "public_address": self.wallet.public_address,
    #         "signature": _signature,
    #         "nonce": _nonce
    #     }, headers={'content-type': 'application/json'})
    #     _json = _res.json()
    #     _access_token = get(_json, 'data.access_token', default=None)
    #     self.client.headers = {
    #         'Authorization': f'Bearer {_access_token}'
    #     }

    @task
    def get_marketplace(self):
        obj = self.client.get(f'/v1/marketplace')


    @task
    def get_marketplace_report(self):
        obj = self.client.get(f'/v1/marketplace/report')

        
    @task
    def get_marketplace_nft_detail(self):
        obj = self.client.get(f'/v1/marketplace/report/nft', params={
            'contract': "0xe6eac9440270750f1d444676335a94205e764969",
            'token_id': 1
        })    

    
    # @task
    # def submit_marketplace_event(self):
    #     obj = self.client.post(f'/v1/marketplace/event', json={
    #         "txn_hash": "0xDA8b7341a9C8E2a7E4e5eC384Fe70b9F9bF8DF36",
    #         "address": "0x8204f26687bed8a8c4c3dd8cb6fba5cb5160e34084130b6f2afe944f706b1830"
    #     }, headers={'content-type': 'application/json'}) 
      

