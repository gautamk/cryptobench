import timeit

from Crypto.Cipher import AES, DES3

from constants import *
from util import get_plain_text, get_key, get_iv


class BaseBackend(object):
    def __init__(self):
        super(BaseBackend, self).__init__()
        self.plain_text = get_plain_text()
        self.cipher_text = None

    def encipher(self):
        raise NotImplementedError()

    def decipher(self):
        raise NotImplementedError()

    def benchmark(self):
        return {
            ENCRYPTION: round(timeit.timeit(self.encipher, number=ITERATIONS), 3),
            DECRYPTION: round(timeit.timeit(self.decipher, number=ITERATIONS), 3)
        }


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


class PyCryptoBase(BaseBackend):
    def encipher(self):
        self.cipher_text = self.algorithm.encrypt(self.plain_text)

    def decipher(self):
        self.algorithm.decrypt(self.cipher_text)


class CryptographyIOBase(BaseBackend):
    def encipher(self):
        encryptor = self.algorithm.encryptor()
        self.cipher_text = encryptor.update(self.plain_text) + encryptor.finalize()

    def decipher(self):
        decryptor = self.algorithm.decryptor()
        decryptor.update(self.cipher_text) + decryptor.finalize()


class OSCryptoBase(BaseBackend):
    def encipher(self):
        args = [self.key, self.plain_text]
        if hasattr(self, 'IV'):
            args.append(self.IV)

        self.cipher_text = self.encrypt(*args)[1]
        print self.cipher_text

    def decipher(self):
        args = [self.key, self.cipher_text]
        if hasattr(self, 'IV'):
            args.append(self.IV)

        self.decrypt(*args)
