# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""

import json
import sys
from time import sleep

from eth_account import Account
import random
import string

from pydash import get

sys.path.append(".")

from helper.wallet import Wallet

OUTPUT_ACCOUNT_DIRECTION = 'fake_stag_accounts.json'


def generate_wallet(quantity=1):
    accounts = []
    letters = string.ascii_letters
    for i in range(quantity):
        pass_phrase = f"{''.join(random.choice(letters) for letter in range(10))} {''.join(random.choice(letters) for letter in range(10))}"
        account = Account.create(pass_phrase)
        address = account.address
        private_key = account.key.hex()
        print('-' * 10)
        print(f'Genrate account # {i}')
        print('address: ', address)
        print('key: ', private_key)
        print('Run gen admin account: ')
        _wallet = Wallet(
            public_address=address,
            private_key=private_key,
            host='https://api-stag.rinz.io'
        )
        obj = _wallet.get('/v1/id/auth/message', params={
            'public_address': _wallet.public_address
        })
        _json = obj.json()
        print('_json', _json)
        _msg = get(_json, 'data.sign_msg')
        _signature = _wallet.sign_msg(_msg)
        _nonce = get(_json, 'data.nonce')

        _res = _wallet.post(f"/v1/id/auth/login", json={
            "public_address": _wallet.public_address,
            "signature": _signature,
            "nonce": _nonce
        })
        sleep(1)
        #  Create admin
        print("*" * 5, "Create account admin")
        _res = _wallet.post(f"/v1/id/iapi/kol_admin", json={
            "username": address,
            "password": address,
            "public_address": address
        })
        accounts.append({
            'pass_phrase': pass_phrase,
            'address': address,
            'private_key': private_key
        })

    writer = open(OUTPUT_ACCOUNT_DIRECTION, 'a')
    writer.write(json.dumps(accounts))
    writer.close()


if __name__ == '__main__':
    generate_wallet(quantity=1000)
