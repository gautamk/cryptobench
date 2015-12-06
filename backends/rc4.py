from Crypto.Cipher import ARC4
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms
from oscrypto.symmetric import rc4_encrypt, rc4_decrypt

from backends.base.algorithm import *
from backends.base.library import *


class PyCrypto(RC4Base, PyCryptoBase):
    def __init__(self):
        super(PyCrypto, self).__init__()
        self.algorithm = ARC4.new(self.key)


class CryptographyIO(RC4Base, CryptographyIOBase):
    def __init__(self):
        super(CryptographyIO, self).__init__()
        self.algorithm = ciphers.Cipher(algorithms.ARC4(self.key),
                                        mode=None,
                                        backend=default_backend())


class OSCrypto(RC4Base, OSCryptoBase):
    def __init__(self):
        super(OSCrypto, self).__init__()
        self.encrypt = rc4_encrypt
        self.decrypt = rc4_decrypt
