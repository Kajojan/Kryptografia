def nwd(a, b):
    while a != b:
        if ( a> b):
            a=a-b
        else:
            b=b-a
    return a


def kodowanie_afinicznie():
    szyfr = ""
    with open("./plain.txt", "r") as f:
        zdanie = f.read()
        zdanie = zdanie.replace('\n', ' ')
 
    with open("./key.txt", 'r') as f:
        key_a = f.readline().split(" ")
        key_b= int(key_a[1])
        key_a=int(key_a[0])
        if key_a < 0 or nwd(key_a, 26) != 1:
            return f"Wrong key: {key_a}"
        if key_b < 0:
            return f"Wrong key: {key_b}"
    for litera in zdanie:
        a = ord(litera)
        if a in range(65, 91):
            a-=65
            a = a * key_a + key_b
            a=a%26
            a+=65
        if a in range(97, 123):
            a-=97
            a = a * key_a + key_b
            a=a%26
            a+=97
        szyfr += chr(a)


    with open("./crypto.txt", "w") as f:
        f.write(szyfr)
 
    return szyfr



def odszyfrowanie_afiniczne():
    zdanie = ""
    with open("./crypto.txt", "r") as f:
        szyfr = f.read()
        szyfr = szyfr.replace('\n', ' ')
 
    with open("./key.txt", 'r') as f:
        key_a = f.readline().split(" ")
        key_b= int(key_a[1])
        key_a=int(key_a[0])
        if key_a < 0 or nwd(key_a, 26) != 1:
            return f"Wrong key: {key_a}"
        if key_b < 0:
            return f"Wrong key: {key_b}"
 
    for litera in szyfr:
        a = ord(litera)
        if a in range(65, 91):
            a-=65
            a = (a - key_b) *  pow(key_a, -1, 26) 
            # a·a` (mod 26) == 1 .      
            a=a%26
            a+=65
        if a in range(97, 123):
            a-=97
            a = (a - key_b) * pow(key_a, -1, 26)
            a=a%26
            a += 97
        zdanie += chr(a)
 
    with open("./decrypt.txt", "w") as f:
        f.write(zdanie)
 
    return zdanie


def literka(a):
    if a in range(65, 91):
            a-=65
    if a in range(97, 123):
            a-=97
    return a

def kryptoanaliza_z_tekstem_jawnym_afiniczny():
    zdanie =""
    with open("./crypto.txt", "r") as f:
        szyfr = f.read()
        szyfr = szyfr.replace('\n', ' ')
        szyfr = szyfr.replace(' ', ' ')
 
    with open("./extra.txt", "r") as f:
        tekstjawny = f.read()
        tekstjawny = tekstjawny.replace('\n', ' ')
        tekstjawny = tekstjawny.replace(' ', '')

    x1 = literka(ord(szyfr[0]))
    x2 = literka(ord(szyfr[1]))
    y1 = literka(ord(tekstjawny[0]))
    y2 = literka(ord(tekstjawny[1]))
    if y1-y2 >=26 or nwd(abs(y1-y2) , 26) != 1:
        print("nie możliwe aby znaleść klucz")
        return f"nie możliwe "
    key_a = ((x1-x2) * pow((y1-y2), -1, 26))%26
    if key_a < 0 :
        key_a+=26
    key_b =x1-((key_a*y1)%26)
    if key_b < 0:
        key_b+=26
    

    for litera in szyfr:
        a = ord(litera)
        if a in range(65, 91):
            a-=65
            a = (a - key_b) *  pow(key_a, -1, 26) 
            # a·a` (mod 26) == 1 .      
            a=a%26
            a+=65
        if a in range(97, 123):
            a-=97
            a = (a - key_b) * pow(key_a, -1, 26)
            a=a%26
            a += 97
        zdanie += chr(a)

    with open("./decrypt.txt", "w") as f:
        f.write(zdanie)
    with open("./key-found.txt", "w") as f:
        f.write(f"{key_a} {int(key_b)}")
    return f"b: {key_b}, a: {int(key_a)}"
        
    



def kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram_afiniczny():
    zdanie = ""
    with open("./crypto.txt", "r") as f:
        szyfr = f.read()
        szyfr = szyfr.replace('\n', ' ')
    with open("./decrypt.txt", "w") as f:
        for key_b in range(1, 27):
            for key_a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                for character in szyfr:
                    a = ord(character)
                    if a in range(65, 91):
                        a-=65
                        a = (a - key_b) * key_a 
                        a=a%26
                        a+=65
                    if a in range(97, 123):
                        a-=97
                        a = (a - key_b) * key_a
                        a=a%26
                        a += 97
                    zdanie += chr(a)
                zdanie += "\n"
                f.write(zdanie)
                zdanie = ""
 
    return "koniec"