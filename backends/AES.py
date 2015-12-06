from Crypto.Cipher import AES
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from oscrypto.symmetric import aes_cbc_pkcs7_encrypt, aes_cbc_pkcs7_decrypt

from backends.base.algorithm import AESBase
from backends.base.library import PyCryptoBase, CryptographyIOBase, OSCryptoBase


class PyCrypto(AESBase, PyCryptoBase):
    def __init__(self):
        super(PyCrypto, self).__init__()
        self.algorithm = AES.new(self.key, mode=AES.MODE_CBC, IV=self.IV)


class CryptographyIO(AESBase, CryptographyIOBase):
    """
    CryptograpyIO makes it unnecessarily verbose
    by requiring the user get and encryptor / decryptor and then calling the finalize method instead of just having an encrypt / decrypt method
    """

    def __init__(self):
        super(CryptographyIO, self).__init__()
        self.algorithm = ciphers.Cipher(algorithms.AES(self.key), modes.CBC(self.IV), backend=default_backend())


class OSCrypto(AESBase, OSCryptoBase):
    def __init__(self):
        super(OSCrypto, self).__init__()
        self.encrypt = aes_cbc_pkcs7_encrypt
        self.decrypt = aes_cbc_pkcs7_decrypt
