from Crypto.Cipher import AES, DES3

from backends import BaseBackend
from util import get_key, get_iv


class AESBase(BaseBackend):
    def __init__(self):
        super(AESBase, self).__init__()
        self.key = get_key(32)
        self.IV = get_iv(AES.block_size)


class TripleDESBase(BaseBackend):
    def __init__(self):
        super(TripleDESBase, self).__init__()
        self.key = get_key(16)
        self.IV = get_iv(DES3.block_size)


class RC4Base(BaseBackend):
    def __init__(self):
        super(RC4Base, self).__init__()
        self.key = get_key(16)


class HashBase(BaseBackend):
    def __init__(self):
        super(HashBase, self).__init__()
        self.algorithm = None

    def decipher(self):
        pass

    def encipher(self):
        self.algorithm(self.plain_text)
