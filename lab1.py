import hashlib
import random
import string


def sha_384(message):

    m = message.encode()
    h = hashlib.sha384(m).hexdigest()

    return h


print(sha_384('hello'))

    
