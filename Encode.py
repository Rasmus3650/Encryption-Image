import base64

key = "AAAAAYjbJHghjGVhB"


test = []
liste = []
liste2 = []
with open("img.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(len(str))
    string = str.decode()
    print(string)
    test.append(string)
    for i in range(len(key)):
        count = 0
        for k in liste:
            if k < ord(key[i]):
                count += 1

        string = string[:ord(key[i]) - 64 + count] + key[i] + string[ord(key[i]) - 64 + count:]
        liste.append(ord(key[i]))


    print(string)

string = string.encode()
print(string)
#print(int.from_bytes(str, "big"))
pic = base64.b64decode(string)
print(pic)
filename = 'encoded_image.png'
with open(filename, 'wb') as f:
    f.write(pic)