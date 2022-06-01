# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import json
from time import sleep

import requests

from util import sign_data, print_done

number = 5000
accounts = []

prefix = "test"
if __name__ == '__main__':
    for fake_number in range(number):

        _payload = {
            "username": f"{prefix}_{fake_number}",
            "password": "000000"
        }

        _url = f'https://api.rinz.io/v1/id/auth/admin/gen_account'

        payload = json.dumps(_payload)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", _url, headers=headers, data=payload)
        # print(response.text)
        accounts.append({
            'name': f"{prefix}_{fake_number}",
            "password": "000000"
        })
        sleep(2)
        print_done(f"gen: {fake_number}")

jsonString = json.dumps(accounts)
jsonFile = open("fake_accounts.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
