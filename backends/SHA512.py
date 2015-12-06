import hashlib

from Crypto.Hash import SHA512
from cryptography.hazmat.backends import openssl
from cryptography.hazmat.primitives import hashes

from backends.base.algorithm import HashBase


class Native(HashBase):
    def __init__(self):
        super(Native, self).__init__()
        self.algorithm = hashlib.sha512


class PyCrypto(HashBase):
    def __init__(self):
        super(PyCrypto, self).__init__()
        h = SHA512.new()
        self.algorithm = h.update


class CryptographyIO(HashBase):
    def __init__(self):
        super(CryptographyIO, self).__init__()
        digest = hashes.Hash(hashes.SHA512(), backend=openssl.backend)
        self.algorithm = digest.update
