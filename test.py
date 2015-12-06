import json
from multiprocessing import Pool

from cipherprofile.block_ciphers import aes, triple_des

modules = {
    'AES': aes,
    'TripleDES': triple_des
}


def _benchmark(backend_instance):
    return backend_instance.benchmark()


def test():
    results = {}
    pool = Pool(3)
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
