from Crypto.Cipher import DES3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from oscrypto.symmetric import tripledes_cbc_pkcs5_decrypt, tripledes_cbc_pkcs5_encrypt

from backends.base import TripleDESBase, PyCryptoBase, CryptographyIOBase, OSCryptoBase


class PyCrypto(TripleDESBase, PyCryptoBase):
    def __init__(self):
        super(PyCrypto, self).__init__()
        self.algorithm = DES3.new(self.key, mode=DES3.MODE_CBC, IV=self.IV)


class CryptographyIO(TripleDESBase, CryptographyIOBase):
    def __init__(self):
        super(CryptographyIO, self).__init__()
        self.algorithm = ciphers.Cipher(algorithms.TripleDES(self.key), modes.CBC(self.IV), backend=default_backend())


class OSCrypto(TripleDESBase, OSCryptoBase):
    def __init__(self):
        super(OSCrypto, self).__init__()
        self.encrypt = tripledes_cbc_pkcs5_encrypt
        self.decrypt = tripledes_cbc_pkcs5_decrypt
