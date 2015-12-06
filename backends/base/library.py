import pyelliptic

from backends import BaseBackend


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

    def decipher(self):
        args = [self.key, self.cipher_text]
        if hasattr(self, 'IV'):
            args.append(self.IV)

        self.decrypt(*args)


class PyEllipticBase(BaseBackend):
    def encipher(self):
        ctx = pyelliptic.Cipher(self.key, self.IV, 1, ciphername=self.ciphername)
        self.cipher_text = ctx.update(self.plain_text) + ctx.final()

    def decipher(self):
        ctx = pyelliptic.Cipher(self.key, self.IV, 0, ciphername=self.ciphername)
        ctx.ciphering(self.cipher_text)