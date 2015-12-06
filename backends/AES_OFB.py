from Crypto.Cipher import AES
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import ciphers
from cryptography.hazmat.primitives.ciphers import algorithms, modes

from backends.base import AESBase, PyCryptoBase, CryptographyIOBase, PyEllipticBase


class PyCrypto(AESBase, PyCryptoBase):
    def __init__(self):
        super(PyCrypto, self).__init__()
        self.algorithm = AES.new(self.key, mode=AES.MODE_OFB, IV=self.IV)


class CryptographyIO(AESBase, CryptographyIOBase):
    """
    CryptograpyIO makes it unnecessarily verbose
    by requiring the user get and encryptor / decryptor and then calling the finalize method instead of just having an encrypt / decrypt method
    """

    def __init__(self):
        super(CryptographyIO, self).__init__()
        self.algorithm = ciphers.Cipher(algorithms.AES(self.key),
                                        modes.OFB(self.IV),
                                        backend=default_backend())


class PyElliptic(AESBase, PyEllipticBase):
    def __init__(self):
        super(PyEllipticBase, self).__init__()
        self.ciphername = 'aes-256-ofb'
