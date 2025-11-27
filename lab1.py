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


def message_list():
    
    pib = 'Навроцька Іванна Аркадіївна'
    messages = []
    
    for i in range(100):
        piece = ''.join(random.choice(string.ascii_letters + string.digits) for j in range(5))
        messages.append(f'{pib} {piece}')
        
    return messages
        

def pre1(messages):

    with open('pre1_res.txt', 'w', encoding='utf-8') as f:

        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384(my_message)
            my_hash16 = my_hash[-4:]

            n = 1
            k = 1
      
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
            f.write('\n\n')

    print('the end')


#messages =  message_list()
#pre1(messages)


def random_changes(m):
    
    allowed = string.ascii_letters + string.digits + string.punctuation

    m_list = list(m)
    num_changes = random.randint(1, len(m_list))
    positions = random.sample(range(len(m_list)), num_changes)

    for pos in positions:
        m_list[pos] = random.choice(allowed)

    res = ''.join(m_list)

    return res


def pre2(messages):

    with open('pre2_res.txt', 'w', encoding='utf-8') as f:

        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384(my_message)
            my_hash16 = my_hash[-4:]

            n = 1
            k = 1
      
            f.write(f'повідомлення: {my_message}, геш повідомлення: {my_hash}\n')
        
            new_message = random_changes(my_message)
            new_hash = sha_384_16(new_message)

            while new_hash != my_hash16:

                if k <= 30:
                    f.write(f'{n}: {new_message}, {new_hash}\n')
                    k += 1
                
                n += 1
                new_message = random_changes(my_message)
                new_hash = sha_384_16(new_message)
        
            f.write(f'останнє значення: {n}: {new_message}, {new_hash}')
            f.write('\n\n')

    print('the end')


#messages =  message_list()
#pre2(messages)


def coll1(messages):
    
    with open('coll1_res.txt', 'w', encoding='utf-8') as f:

        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384(my_message)
            my_hash16 = my_hash[-4:]

            n = 1
            k = 1
      
            f.write(f'повідомлення: {my_message}, геш повідомлення: {my_hash}\n')

            for_coll = {}

            while True:
                new_message = my_message + str(n)
                new_hash = sha_384_32(new_message)

                if new_hash in for_coll:
                    f.write(f'{n}: Є колізія:{new_message},{new_hash} і {for_coll[new_hash]},{new_hash}\n')
                    f.write('\n\n')
                    break

                for_coll[new_hash] = new_message

                if k <= 30:
                    f.write(f'{n}: {new_message}, {new_hash}\n')
                    k += 1

                n += 1

    print('the end')


messages =  message_list()
coll1(messages)    

    






        

    



    
