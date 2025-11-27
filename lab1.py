import hashlib
import random
import string


def sha_384(message):

    m = message.encode()
    h = hashlib.sha384(m).hexdigest()

    return h


my_message = 'Я Навроцька Іванна Аркадіївна'
my_hash = sha_384(my_message)
print(my_hash)


def pre():

    my_message = 'Я Навроцька Іванна Аркадіївна'
    my_hash = sha_384(my_message)
    hash_16bits = my_hash[-4:]

    n = 1
    new_message = my_message + str(n)
    new_hash = sha_384(new_message)
    new_hash_16bits = new_hash[-4:]

    k = 1
    
    while new_hash_16bits != hash_16bits:
        n += 1
        new_message = my_message + str(n)
        new_hash = sha_384(new_message)
        new_hash_16bits = new_hash[-4:]
        k += 1
        print(k)
        print(new_hash)


pre()

        

    



    
