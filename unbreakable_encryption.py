from secrets import token_bytes
from typing import Tuple
import base64

def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    #print(tb)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    # big betyder, at mest betydende bit er i starten (venstre), altså den bit, der repræsentere den højeste numeriske værdi
    print(original_key)
    print(dummy)
    encrypted: int = original_key ^ dummy  # XOR
    print("\n")
    print(encrypted)
    return dummy, encrypted, original_key

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    with open("img.png", "rb") as imageFile:
        stri = base64.b64encode(imageFile.read())
        string = stri.decode()
        #print("af" + str(string))
    key1, key2, original = encrypt(string)
    #print(key1)
    #print(key2)
    #print(original)
    result: str = decrypt(key1, key2)
    #print(result)
    pic = base64.b64decode(result)
    filename = 'new_image.png'
    with open(filename, 'wb') as f:
        f.write(pic)
