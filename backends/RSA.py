import timeit

from Crypto.PublicKey import RSA
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from oscrypto.asymmetric import generate_pair, rsa_oaep_encrypt, rsa_oaep_decrypt

from backends import BaseBackend
from constants import ENCRYPTION, DECRYPTION

KEY_SIZE = 1024
CHUNK_RATIO = 500000


class BaseAsymetric(BaseBackend):
    def __init__(self):
        super(BaseAsymetric, self).__init__()
        self.chunk_count, self.chunk_size = len(self.plain_text), len(self.plain_text) / CHUNK_RATIO
        self.chunks = [self.plain_text[i:i + self.chunk_size] for i in range(0, self.chunk_count, self.chunk_size)]
        self.chunks_len = len(self.chunks)

    def decipher(self):
        for i, chunk in enumerate(self.cipher_text):
            self._decipher(chunk)

    def _decipher(self, cipher_text):
        raise NotImplementedError()

    def encipher(self):
        self.cipher_text = []
        for i, chunk in enumerate(self.chunks):
            self.cipher_text.append(self._encipher(chunk))

    def _encipher(self, plain_text):
        raise NotImplementedError

    def benchmark(self):
        return {
            ENCRYPTION: round(timeit.timeit(self.encipher, number=1), 3),
            DECRYPTION: round(timeit.timeit(self.decipher, number=1), 3)
        }


class PyCrypto(BaseAsymetric):
    def _encipher(self, plain_text):
        return self.key.encrypt(plain_text, None)

    def _decipher(self, cipher_text):
        self.key.decrypt(cipher_text)

    def __init__(self):
        super(PyCrypto, self).__init__()
        self.key = RSA.generate(KEY_SIZE)


class CryptographyIO(BaseAsymetric):
    def _decipher(self, cipher_text):
        self.key.decrypt(
            cipher_text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
            )
        )

    def _encipher(self, plain_text):
        public_key = self.key.public_key()
        return public_key.encrypt(
            plain_text,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
            )
        )

    def __init__(self):
        super(CryptographyIO, self).__init__()
        self.key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=KEY_SIZE,
            backend=default_backend()
        )


class OSCrpto(BaseAsymetric):
    def __init__(self):
        super(OSCrpto, self).__init__()
        self.key = generate_pair('rsa', bit_size=KEY_SIZE)

    def _encipher(self, plain_text):
        return rsa_oaep_encrypt(self.key[0], plain_text)

    def _decipher(self, cipher_text):
        rsa_oaep_decrypt(self.key[1], cipher_text)
