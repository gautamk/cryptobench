import timeit

from constants import ENCRYPTION, ITERATIONS, DECRYPTION
from util import get_plain_text


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
