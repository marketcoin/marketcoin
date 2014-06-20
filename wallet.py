import config
import binascii
import ecdsa
import random

system_random = random.SystemRandom()


def key_to_string(key):
    return binascii.hexlify(key.to_string()).decode('utf-8')


class Wallet:
    def __init__(self):
        # labels, indexed on private key
        # TODO: public key support
        self.labels = {}
        with config.open('keys.txt', 'rb') as f:
            for line in f.readlines():
                key, label = line.split(b':', 1)
                key = binascii.unhexlify(key)
                label = label.strip()
                self.labels[key] = label.decode('utf-8')

    def generate_address(self, label: str):
        label = label.strip()
        # TODO: introduce extra entropy
        secret = system_random.randrange(ecdsa.SECP256k1.order)
        private_key = ecdsa.SigningKey.from_secret_exponent(secret, curve=ecdsa.SECP256k1)
        with config.open('keys.txt', 'ab') as f:
            f.write(key_to_string(private_key).encode('utf-8') + b':' + label.encode('utf-8') + b'\n')
        self.labels[key_to_string(private_key)] = label
        public_key = private_key.get_verifying_key()
        return key_to_string(public_key)