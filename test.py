import json

from cipherprofile.asymmetric import rsa, ecies
from cipherprofile.block_ciphers import aes, triple_des
from cipherprofile.hashes import md5, sha512
from cipherprofile.stream_ciphers import rc4, aes_ofb

modules = {
    # 'AES': aes,
    # 'TripleDES': triple_des,
    # 'RC4': rc4,
    # 'AES_OFB': aes_ofb,
    # 'MD5': md5,
    # 'SHA512': sha512,
    # 'RSA': rsa,
    'ECIES': ecies
}


def _benchmark(backend_instance):
    return backend_instance.benchmark()
    # try:
    #     pass
    # except Exception as e:
    #     return {
    #         'error': str(e)
    #     }


def test():
    results = {}
    for algorithm_name, module in modules.iteritems():
        results[algorithm_name] = {}
        print "Algorithm " + algorithm_name
        for backend in module.backends:
            instance = backend()
            backend_name = backend.__name__
            print "\tTesting library " + backend_name
            results[algorithm_name][backend_name] = _benchmark(instance)
    return results


if __name__ == "__main__":
    print json.dumps(test(), indent=2)
