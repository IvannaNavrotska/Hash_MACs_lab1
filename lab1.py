import hashlib
import random
import string


def sha_384(message):

    m = message.encode()
    h = hashlib.sha384(m).hexdigest()
    
    return 


def sha_384_16(message):

    m = message.encode()
    h = hashlib.sha384(m).hexdigest()
    h_16 = h[-4:]
    
    return h_16


def sha_384_32(message):

    m = message.encode()
    h = hashlib.sha384(m).hexdigest()
    h_32 = h[-8:]
    
    return h_32



def pre():

    my_message = 'Я Навроцька Іванна Аркадіївна'
    my_hash = sha_384(my_message)
    hash_16bits = my_hash[-4:]

    n = 0
    k = 0

    with open(pre1_res.txt, 'w') as f:
        
        new_message = my_message + str(n)
        new_hash = sha_384(new_message)
        new_hash_16bits = new_hash[-4:]

    
        while new_hash_16bits != hash_16bits:

            if k < 30:
                f.write(f'{n}: {new_message}, {new_hash}')
                k += 1
                
        n += 1
        new_message = my_message + str(n)
        new_hash = sha_384(new_message)
        new_hash_16bits = new_hash[-4:]
        


pre()

        

    



    
