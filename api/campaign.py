# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from locust import HttpUser, constant_throughput, task
from pydash import get

from helper.wallet import Wallet
import json

with open("fake_stag_accounts.json") as f:
    accounts = json.load(f)


class TestCampaign(HttpUser):
    wait_time = constant_throughput(1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _account = accounts.pop()
        print(_account)
        self.wallet = Wallet(
            public_address=get(_account, 'address'),
            private_key=get(_account, 'private_key'),
            host=''
        )

    def on_start(self):
        """
        - Login
        :return:
        """

        obj = self.client.get('/v1/id/auth/message', params={
            'public_address': self.wallet.public_address
        })
        _json = obj.json()

        _msg = get(_json, 'data.sign_msg')
        _signature = self.wallet.sign_msg(_msg)
        _nonce = get(_json, 'data.nonce')
        print(_signature)

        _res = self.client.post("/v1/id/auth/login", json={
            "public_address": self.wallet.public_address,
            "signature": _signature,
            "nonce": _nonce
        }, headers={'content-type': 'application/json'})
        _json = _res.json()
        _access_token = get(_json, 'data.access_token', default=None)
        self.client.headers = {
            'Authorization': f'Bearer {_access_token}'
        }

    @task
    def get_list_owned_campaigns(self):
        obj = self.client.get(f'/v1/campaign/get_list')

    @task
    def get_details_of_campaign(self):
        obj = self.client.get('/v1/campaign/details')

    @task
    def get_details_campaign_admin_site(self):
        campaign_id = ""
        obj = self.client.get(f'/v1/campaign/admin/details/{campaign_id}')

    @task
    def get_hot_campaigns(self):
        obj = self.client.get("/v1/campaign/hot")

    @task
    def get_nft_type_details(self):
        _payload = {
            "contract_address": "",
            "index_type": 1
        }
        obj = self.client.post("/v1/campaign/nft_details", _payload)

