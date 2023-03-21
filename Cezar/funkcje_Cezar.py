
def kodowanie():
    szyfr = ""
 
    with open("Kryptografia/Cezar/plain.txt", "r") as f:
        zdanie = f.read()
        zdanie = zdanie.replace('\n', ' ')
 
    with open("Kryptografia/Cezar/key.txt", 'r') as f:
        key = int(f.readline().split(" ")[0])
        if key < 0:
            return f"Wrong key: {key}"
        key = key % 26
 
    for litera in zdanie:
        a = ord(litera)
        if a in range(65, 91): #Wielkie litery
            a += key
            if a > 90:
                a = a - 26
        if a in range(97, 123):

            a += key
            if a > 122:
               
                a = a - 26
              
        szyfr += chr(a)
 
    with open("Kryptografia/Cezar/crypto.txt", "w") as f:
        f.write(szyfr)
 
    return szyfr
 

def odszyfrowanie():
    zdanie = ""
    with open("Kryptografia/Cezar/crypto.txt", "r") as f:
        szyfr = f.read()
        szyfr = szyfr.replace('\n', ' ')
 
    with open("Kryptografia/Cezar/key.txt", 'r') as f:
        key = int(f.readline().split(" ")[0])
        if key < 0:
            return "Wrong key: {}".format(key)
        key = key % 26
        print(key)

 
    for litera in szyfr:
        a = ord(litera)
        if a in range(65, 91):
            a -= key
            if a < 65:
                a = a + 26
        if a in range(97, 123):
            a -= key
            if a < 97:
                a = a + 26
        zdanie += chr(a)
 
    with open("Kryptografia/Cezar/decrypt.txt", "w") as f:
        f.write(zdanie)
 
    return zdanie


def kryptoanaliza_z_tekstem_jawnym():
    with open("Kryptografia/Cezar/crypto.txt", "r") as f:
        szyfr = f.read()
        szyfr = szyfr.replace('\n', ' ')
 
    with open("Kryptografia/Cezar/extra.txt", "r") as f:
        tekst_jawny = f.read()
        tekst_jawny = tekst_jawny.replace('\n', ' ')
        tekst_jawny = tekst_jawny.split(" ")
 
    for index, slowo in enumerate(szyfr):
        for index2, litera in enumerate(slowo):
            if ord(litera) in range(65, 91) or ord(litera) in range(97, 123):
                print(ord(litera), " - ",ord(tekst_jawny[index][index2]) )
                key = (ord(litera) - ord(tekst_jawny[index][index2])) % 26
                with open("Kryptografia/Cezar/key-found.txt", "w") as f:
                    f.write(str(key))
                return key
 
    key = "Error- nie znalezionow klucza "
 
    with open("Kryptografia/Cezar/key-found.txt", "w") as f:
        f.write(str(key))
 
    return key
 
def kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram():
    zdanie = ""
    with open("Kryptografia/Cezar/crypto.txt", "r") as f:
        szyfr = f.read()
        szyfr = szyfr.replace('\n', ' ')
    with open("Kryptografia/Cezar/decrypt.txt", "w") as f:
        for key in range(1, 26):
            for litera in szyfr:
                a = ord(litera)
                if a in range(65, 91):
                    a -= key
                    if a < 65:
                        a = a + 26
                if a in range(97, 123):
                    a -= key
                    if a < 97:
                        a = a + 26
                zdanie += chr(a)
            zdanie += "\n"
            f.write(zdanie)
            zdanie = ""
 
    return "Done"

