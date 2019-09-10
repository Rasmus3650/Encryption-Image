import random
import string

def keyGen():
    user_key = ''
    for i in range(random.randint(9,17)):
        char = random.randint(0,51)
        partial_key = string.ascii_letters[char]
        user_key += user_key.join(partial_key)
    user_key = user_key.lower()
    return user_key
