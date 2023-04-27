#Kajetan Jankowski

import random
from PIL import Image
import hashlib



block_size = 4

keys = []
for x in range(block_size):
    # key = bytes([random.randint(0, 255) for j in range(block_size+1)])
    key = hashlib.sha1(str(x ** 12 + x).encode("UTF-8")).digest()
    keys.append(key)



Zdjecie = Image.open("plain.bmp")
Zdjecie_bajty = Zdjecie.tobytes()
wymiary = Zdjecie.size
Zdjecie_bajty_nowe = []
for x in range(wymiary[1]):
    for y in range(wymiary[0]):
        pp = x * wymiary[0]  + y 
        op = Zdjecie_bajty[pp]
        pta = op ^ keys[x % block_size][y % block_size]
        Zdjecie_bajty_nowe.append(pta)

def Zapisz(data, AS ):
    output_image = Zdjecie.copy()
    output_image.frombytes(bytes(data))
    output_image.save(AS)


Zapisz(Zdjecie_bajty_nowe, "ecb_crypto.bmp")

new_key = 8
Zdjecie_bajty_nowe = [Zdjecie_bajty[0] ^ new_key]
for x in range(wymiary[0] * wymiary[1]):
    Zdjecie_bajty_nowe.append(Zdjecie_bajty_nowe[x - 1] ^ Zdjecie_bajty[x] ^ keys[x % (block_size*block_size) // block_size][x % block_size] )

Zapisz(Zdjecie_bajty_nowe, "cbc_crypto.bmp")


