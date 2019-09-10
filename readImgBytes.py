import base64

key = "UYyGUhnikNnNjNNJLJNINobINFInUYGkyBKJbiuTGUKJhbkYGiujhbJYvKJVkyjvYVuyUB"

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

        string = string[:ord(key[i]) + count] + key[i] + string[ord(key[i]) + count:]
        liste.append(ord(key[i]))


    print(string)

    for i in range(len(key)):
        count = 0
        for k in liste2:
            if k < ord(key[i]):
                count -= 1

        count2 = 0
        for k in liste:
            if k < ord(key[i]):
                count += 1

        string = string[:ord(key[i]) + count] + string[ord(key[i]) + 1 + count:]
        liste2.append(ord(key[i]))
    print(string)
    test.append(string)
    string = string.encode()
    print(string)
    #print(int.from_bytes(str, "big"))
    if (test[0] == test[1]):
        print("YOINKS")
    pic = base64.b64decode(string)
    print(pic)
    filename = 'new_image.png'
    with open(filename, 'wb') as f:
        f.write(pic)