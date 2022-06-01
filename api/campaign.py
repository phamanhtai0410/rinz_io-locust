# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import json
from datetime import datetime, timedelta
from time import sleep
import pydash
from locust import HttpUser, task, between, constant_throughput
from random import choice, random, uniform, choices, randint

# Opening JSON file
# Load account for test
with open('/fake_accounts.json', "r") as f:
    fake_accounts = json.load(f)


def convert_datetime_to_string(date: datetime,
                               _format="%Y%m%d%H%M%S") -> str:
    return date.strftime(_format)


class TestCampaign(HttpUser):
    wait_time = constant_throughput(1)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.account = None

    def login(self, account):
        obj = self.client.post('/v1/id/auth/admin/login', json=account)
        if obj.status_code != 200:
            print('Login', obj.text)
            raise Exception
        return pydash.get(obj.json(), 'data.access_token')

    def on_start(self):
        _account = fake_accounts.pop()
        self.account = _account
        _token = self.login(self.account)
        self.client.headers = {
            'Authorization': f'Bearer {_token}'
        }

    @task(1)
    def get_list_campaigns(self):
        pass


    #
    # @task(5)
    # def get_batches(self):
    #     obj = self.client.get('/v1/transaction/pos/batches')
    #     if obj.status_code != 200:
    #         print(obj.text)
    #     else:
    #         _data = obj.json()
    #         _sections = pydash.get(_data, 'data.sections', default=[])
    #         if _sections:
    #             _param = choice(_sections)
    #             _trans = self.client.get('/v1/transaction/pos/batch', params=_param)
    #             if _trans.status_code != 200:
    #                 print(_trans.text)

