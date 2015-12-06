from Crypto.Cipher import AES
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from oscrypto.symmetric import aes_cbc_pkcs7_encrypt, aes_cbc_pkcs7_decrypt

from backends.base import BaseBackend
from util import get_key, get_iv


class AESBackend(BaseBackend):
    def __init__(self):
        super(AESBackend, self).__init__()
        self.key = get_key(32)
        self.IV = get_iv(AES.block_size)


class PyCrypto(AESBackend):
    def encipher(self):
        self.cipher_text = self.aes.encrypt(self.plain_text)

    def decipher(self):
        self.aes.decrypt(self.cipher_text)

    def __init__(self):
        super(PyCrypto, self).__init__()
        self.aes = AES.new(self.key, mode=AES.MODE_CBC, IV=self.IV)


class CryptographyIO(AESBackend):
    """
    CryptograpyIO makes it unnecessarily verbose
    by requiring the user get and encryptor / decryptor and then calling the finalize method instead of just having an encrypt / decrypt method
    """

    def encipher(self):
        encryptor = self.aes.encryptor()
        self.cipher_text = encryptor.update(self.plain_text) + encryptor.finalize()

    def decipher(self):
        decryptor = self.aes.decryptor()
        decryptor.update(self.cipher_text) + decryptor.finalize()

    def __init__(self):
        super(CryptographyIO, self).__init__()
        self.aes = ciphers.Cipher(algorithms.AES(self.key), modes.CBC(self.IV), backend=default_backend())


class OSCrypto(AESBackend):
    def __init__(self):
        super(OSCrypto, self).__init__()

    def encipher(self):
        self.cipher_text = aes_cbc_pkcs7_encrypt(self.key, self.plain_text, self.IV)[1]

    def decipher(self):
        aes_cbc_pkcs7_decrypt(self.key, self.cipher_text, self.IV)
