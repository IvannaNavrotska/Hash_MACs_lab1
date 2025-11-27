import hashlib
import random
import string


def sha_384(message):

    m = message.encode()
    h = hashlib.sha384(m).hexdigest()
    
    return h


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

    my_message = 'Навроцька Іванна Аркадіївна'
    my_hash = sha_384(my_message)
    my_hash16 = my_hash[-4:]

    n = 1
    k = 1

    with open('pre1_res.txt', 'w', encoding='utf-8') as f:

        f.write(f'повідомлення: {my_message}, геш повідомлення: {my_hash}\n')
        
        new_message = my_message + str(n)
        new_hash = sha_384_16(new_message)

        while new_hash != my_hash16:

            if k <= 30:
                f.write(f'{n}: {new_message}, {new_hash}\n')
                k += 1
                
            n += 1
            new_message = my_message + str(n)
            new_hash = sha_384_16(new_message)
        
        f.write(f'останнє значення: {n}: {new_message}, {new_hash}')
        

pre()

        

    



    
