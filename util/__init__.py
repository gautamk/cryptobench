import os

__plain_text__ = None
__keys__ = {}


def get_plain_text():
    global __plain_text__
    if not __plain_text__:
        __plain_text__ = os.urandom(5 * 1000 * 1000)
    return __plain_text__


def get_iv(bytesize):
    """
    Get an Initialization Vector
    :param bytesize:
    :return:
    """
    return os.urandom(bytesize)


def get_key(bytesize):
    global __keys__
    key = __keys__.get(bytesize)
    if not key:
        key = __keys__[bytesize] = get_iv(bytesize)
    return key
