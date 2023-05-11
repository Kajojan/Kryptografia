# Kajetan Jankowski

with open("hash.txt", "r") as f:
    hashes = []
    for x in f:
        helper = x.replace(" ", "").replace("-", "").replace("\n", "")
        hashes.append(helper)

dif_tab = []
for x in range(0, len(hashes), 2):
    h1 = "{0:08b}".format(int(hashes[x], 16))
    h2 = "{0:08b}".format(int(hashes[x+1], 16))
    dif = 0
    for x, y in zip(h1, h2):
        if x != y:
            dif += 1
    dif_tab.append(dif)



functions = ["md5sum", "sha1sum", "sha224sum", "sha256sum", "sha384sum", "sha512sum", "b2sum"]
sum = [128, 160, 224, 256, 384, 512, 512]

with open("diff.txt", "w") as f:
    for x in range(0, len(hashes), 2):
        f.write(functions[x//2] + "\n")
        f.write(hashes[x] + "\n")
        f.write(hashes[x+1] + "\n")
        f.write(f"Liczba różniących się bitów: {dif_tab[x//2]} z {sum[x//2]}, procentowo: {round(dif_tab[x//2]/sum[x//2], 2)*100}%" + "\n" + "\n")

with open("diff.txt", "r") as f:
    l = f.read()
    print(l)