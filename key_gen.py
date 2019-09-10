import random
import string

def key_gen():
    user_key = ''
    for i in range(random.randint(4,8)):
        char = random.randint(0,51)
        partial_key = string.ascii_letters[char]
        user_key += user_key.join(partial_key)
    return user_key


key_gen()