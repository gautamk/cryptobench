from backends.AES import PyCrypto, CryptographyIO, OSCrypto

backends = [
    PyCrypto,
    CryptographyIO,
    OSCrypto
]


def test_all():
    results = {}
    for backend in backends:
        instance = backend()
        results[backend.__name__] = instance.benchmark()
    return results
