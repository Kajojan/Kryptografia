# def Odczyt_z_pliku():
#     with open("Cezar/plain.txt", "r") as plik:
#         zawartosc_pliku = plik.read()
#     return zawartosc_pliku


# def Cezar(opcja,x,k):
#     match opcja:
#         case "e":
#             return chr((ord(x) + k - 65) % 26 + 65)
#         case "d":
#             return chr((ord(x) - k - 65) % 26 + 65)


def code_message():
    cryptogram = ""
 
    with open("./plain.txt", "r") as f:
        message = f.read()
        message = message.replace('\n', ' ')
 
    with open("./key.txt", 'r') as f:
        key = int(f.readline().split(" ")[0])
        if key < 0:
            return f"Wrong key: {key}"
        key = key % 26
 
    for character in message:
        a = ord(character)
        if a in range(65, 91):
            a += key
            if a > 90:
                a = a - 26
        if a in range(97, 123):
            a += key
            if a > 122:
                a = a - 26
        cryptogram += chr(a)
 
    with open("./crypto.txt", "w") as f:
        f.write(cryptogram)
 
    return cryptogram
 

def read_code():
    message = ""
    with open("./crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')
 
    with open("./key.txt", 'r') as f:
        key = int(f.readline().split(" ")[0])
        if key < 0:
            return "Wrong key: {}".format(key)
        key = key % 26
 
    for character in cryptogram:
        a = ord(character)
        if a in range(65, 91):
            a -= key
            if a < 65:
                a = a + 26
        if a in range(97, 123):
            a -= key
            if a < 97:
                a = a + 26
        message += chr(a)
 
    with open("./decrypt.txt", "w") as f:
        f.write(message)
 
    return message