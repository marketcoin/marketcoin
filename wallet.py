import config
import binascii
import ecdsa
import random
import requests
import json
from rpc import RPC


my_rpc = RPC()
system_random = random.SystemRandom()


def key_to_string(key):
    return binascii.hexlify(key.to_string()).decode('utf-8')


class Wallet:
    def __init__(self):
        self.transactions = []
        self.public_key = {}

        # labels, indexed on private key
        # TODO: watch-only public key support
        self.labels = {}
        with config.open('keys.txt', 'rb') as f:
            for line in f.readlines():
                key, label = line.split(b':', 1)
                key = binascii.unhexlify(key)
                label = label.strip()
                self.labels[key] = label.decode('utf-8')
                privkey = ecdsa.SigningKey.from_string(key, curve=ecdsa.SECP256k1)
                self.public_key[key] = key_to_string(privkey.get_verifying_key())

    def generate_address(self, label: str):
        label = label.strip()
        # TODO: introduce extra entropy
        secret = system_random.randrange(ecdsa.SECP256k1.order)
        private_key = ecdsa.SigningKey.from_secret_exponent(secret, curve=ecdsa.SECP256k1)
        with config.open('keys.txt', 'ab') as f:
            f.write(key_to_string(private_key).encode('utf-8') + b':' + label.encode('utf-8') + b'\n')
        privkey_hex = key_to_string(private_key)
        self.labels[privkey_hex] = label
        self.public_key[privkey_hex] = key_to_string(private_key.get_verifying_key())
        return self.public_key[privkey_hex]

    def transactions(self):
        ret = []
        for privkey, pubkey in self.public_key.items():
            ret += my_rpc.get_transactions(pubkey)
        return ret

    def balance(self):
        ret = 0
        for privkey, pubkey in self.public_key.items():
            ret += my_rpc.get_balance(pubkey)
        return ret