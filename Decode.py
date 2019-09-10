import base64

def funDecode():
    key = input("Key: ")
    liste = []
    liste2 = []

    for j in key:
        liste.append(ord(j))

    print(liste)

    for i in range(len(key)):
        count = 0
        for k in liste2:
            if k < ord(key[i]):
                count -= 1

        count2 = 0
        for k in liste:
            if k < ord(key[i]):
                count += 1

        string = string[:ord(key[i]) - 64 + count] + string[ord(key[i]) - 64 + 1 + count:]
        liste2.append(ord(key[i]))