import random
import string

def keyGen():
    user_key = ''
    for i in range(random.randint(7,15)):
        char = random.randint(0,51)
        partial_key = string.ascii_letters[char]
        user_key += user_key.join(partial_key)
    return user_key
