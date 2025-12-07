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
    
    last_n = []

    with open('pre1_res.txt', 'w', encoding='utf-8') as f:
        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384_16(my_message)
            
            n = 1
            k = 1
      
            f.write(f'повідомлення: {my_message}, геш повідомлення: {sha_384(my_message)}\n')
        
            new_message = my_message + str(n)
            new_hash = sha_384_16(new_message)

            while new_hash != my_hash:

                if k <= 30:
                    f.write(f'{n}: {new_message}, {sha_384(new_message)}\n')
                    k += 1
                
                n += 1
                new_message = my_message + str(n)
                new_hash = sha_384_16(new_message)
        
            last_n.append(n)

            f.write(f'останнє значення: {n}: {new_message}, {sha_384(new_message)}\n\n')

        f.write(f'{last_n}')

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

    last_n = []

    with open('pre2_res.txt', 'w', encoding='utf-8') as f:

        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384_16(my_message)

            n = 1
            k = 1
      
            f.write(f'повідомлення: {my_message}, геш повідомлення: {sha_384(my_message)}\n')
        
            new_message = random_changes(my_message)
            new_hash = sha_384_16(new_message)

            while new_hash != my_hash:

                if k <= 30:
                    f.write(f'{n}: {new_message}, {sha_384(new_message)}\n')
                    k += 1
                
                n += 1
                new_message = random_changes(my_message)
                new_hash = sha_384_16(new_message)

            last_n.append(n)
            
            f.write(f'останнє значення: {n}: {new_message}, {sha_384(new_message)}')
            f.write('\n\n')
            f.write(f'{last_n}')

    print('the end')


#messages =  message_list()
#pre2(messages)


def coll1(messages):

    last_n = []
    
    with open('coll1_res.txt', 'w', encoding='utf-8') as f:

        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384_32(my_message)

            n = 1
            k = 1
      
            f.write(f'повідомлення: {my_message}, геш повідомлення: {sha_384(my_message)}\n')

            for_coll = {}

            while True:
                new_message = my_message + str(n)
                new_hash = sha_384_32(new_message)
                
                if new_hash in for_coll:
                    f.write(f'{n}: є колізія: {new_message}, {sha_384(new_message)} і {for_coll[new_hash]}, {sha_384(for_coll[new_hash])}\n')
                    f.write('\n\n')
                    break

                for_coll[new_hash] = new_message

                if k <= 30:
                    f.write(f'{n}: {new_message}, {sha_384(new_message)}\n')
                    k += 1

                n += 1
                
            last_n.append(n)
        f.write(f'{last_n}')

    print('the end')

   
#messages =  message_list()
#coll1(messages)


def coll2(messages):

    last_n = []
    
    with open('coll2_res.txt', 'w', encoding='utf-8') as f:

        for i, my_message in enumerate(messages, 1):

            my_hash = sha_384_32(my_message)

            n = 1
            k = 1
      
            f.write(f'повідомлення: {my_message}, геш повідомлення: {sha_384(my_message)}\n')

            for_coll = {}

            while True:
                new_message = random_changes(my_message)
                new_hash = sha_384_32(new_message)

                if new_hash in for_coll:
                    coll_is = for_coll[new_hash]

                    if new_message != coll_is:
                        f.write(f'{n}: є колізія: {coll_is}, {sha_384(coll_is)} і {new_message}, {sha_384(new_message)}\n\n')
                        break

                for_coll[new_hash] = new_message

                if k <= 30:
                    f.write(f'{n}: {new_message}, {sha_384(new_message)}\n')
                    k += 1

                n += 1
                
            last_n.append(n)
        f.write(f'{last_n}')
            
    print('the end')

#messages =  message_list()
#coll2(messages)
    

messages_p =  message_list()
pre1(messages_p)
pre2(messages_p)


messages_c =  message_list()
coll1(messages_c)
coll2(messages_c)   





        

    



    
