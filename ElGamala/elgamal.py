# Kajetan Jankowski


import random
import sys

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def key_gen():
    with open("elgamal.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
    private_key = random.randint(1, p - 1)

    while gcd(p, private_key) != 1:
        private_key = random.randint(1, p - 1)
    public_key = pow(g, private_key, p)

    with open("public.txt", "w") as f:
        f.write(str(p) + "\n" + str(g) + "\n" + str(public_key))

    with open("private.txt", "w") as f:
        f.write(str(p) + "\n" + str(g) + "\n" + str(private_key))

    print("Keys successfully saved in a files.")
    return True


def encryption():
    with open("public.txt", 'r') as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        public_key = int(f.readline().replace("\n", ''))
    k = random.randint(10 ** 20, p)
    while gcd(p, k) != 1:
        k = random.randint(10 ** 20, p)

    with open("plain.txt", 'r') as f:
        msg = int(f.readline().replace("\n", " "))

    if not msg < p:
        return False

    with open("crypto.txt", "w") as f:
        f.write(str(pow(g, k, p)) + "\n" + str((pow(public_key, k, p) * msg)))
        # f.write(str((power_mod(public_key, k, p) * msg)))

    return True


def decryption():
    with open("crypto.txt", "r") as f:
        gk = int(f.readline().replace("\n", ''))
        msg = int(f.readline().replace("\n", ''))

    with open("private.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        b = int(f.readline().replace("\n", ''))

    key = pow(gk, b, p)
    with open("decrypt.txt", "w") as f:
        f.write(str(int(msg // key)))
    return True


def signature():
    with open("message.txt", "r") as f:
        msg = int(f.readline().replace("\n", ''))

    with open("private.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        b = int(f.readline().replace("\n", ''))

    if not msg < p:
        return False
    
    k = random.randint(1, p - 1)
    while gcd(k, p - 1) != 1:
        k = random.randint(1, p - 1)

    r = pow(g, k, p)
    k_inverse = pow(k, -1, p - 1)
    x = ((msg - b * r) * k_inverse) % (p - 1)
    with open("signature.txt", "w") as f:
        f.write(str(r) + "\n")
        f.write(str(x) + "\n")
    return True


def verify():
    with open("public.txt", 'r') as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        public_key = int(f.readline().replace("\n", ''))

    with open("signature.txt", 'r') as f:
        r = int(f.readline().replace("\n", ''))
        x = int(f.readline().replace("\n", ''))

    with open ("message.txt", 'r') as f :
        msg = int(f.readline().replace("\n", ''))

    v1 = pow(g, msg, p)
    v2 = (pow(r, x, p)) * (pow(public_key, r, p))
    gm = pow(g, msg, p)
    rx_beta_r = (pow(public_key, r, p) * pow(r, x, p)) % p

    print(str(v1) +"\n"+ str((v2 % p)))

    if gm == rx_beta_r:
        with open("verify.txt", "w") as f:
            f.write("True")
        print("Verified: True")
    else:
        with open("verify.txt", "w") as f:
            f.write("False")
        print("Verified: False")

    return True


s1 = sys.argv[1]

todo = False

if s1 in ["-k", "k"]:
    todo = key_gen
elif s1 in ["-e", "e"]:
    todo = encryption
elif s1 in ["-d", "d"]:
    todo = decryption
elif s1 in ["-s", "s"]:
    todo = signature
elif s1 in ["-v", "v"]:
    todo = verify
else:
    print("Wrong parameter: {}".format(s1))

if todo():
    print("Done")
else:
    print("ERROR !!!")
