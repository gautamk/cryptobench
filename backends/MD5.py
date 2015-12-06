import hashlib

from Crypto.Hash import MD5
from cryptography.hazmat.backends import openssl
from cryptography.hazmat.primitives import hashes

from backends.base.algorithm import HashBase


class Native(HashBase):
    def __init__(self):
        super(Native, self).__init__()
        self.algorithm = hashlib.md5


class PyCrypto(HashBase):
    def __init__(self):
        super(PyCrypto, self).__init__()
        h = MD5.new()
        self.algorithm = h.update


class CryptographyIO(HashBase):
    def __init__(self):
        super(CryptographyIO, self).__init__()
        digest = hashes.Hash(hashes.MD5(), backend=openssl.backend)
        self.algorithm = digest.update
