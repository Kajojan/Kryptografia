# Kajetan Jankowski



import sys

def ecrypt_1():
    with open("mess.txt", "r") as f:
        msg = f.readline().strip()
        chars = list(msg.lower())
        binary_seq = ""
        bin_array = []

        for i in chars:
            if i in 'abcdef':
                binary_seq = binary_seq + "{0:b}".format(ord(i) - 87)
            else:
                binary_seq = binary_seq + bin(ord(i)).replace("0b11", "")
        for char in binary_seq:
            bin_array.append(char)
    if len(binary_seq) != 64:
        print("Wiadomość musi miec 64bity")
        return False

    with open('cover.html', 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.rstrip() for line in lines]

    with open("watermark.html", 'w') as file:
        file.write('\n'.join(cleaned_lines))

    with open('watermark.html', 'r') as cover:
        initial_lines = cover.readlines()

        with open("watermark.html", "w") as f:
            for i in range(0, len(initial_lines)):
                if i < len(bin_array) and bin_array[i] == '1':
                    modified_line = initial_lines[i].rstrip('\n') + ' ' + '\n'
                    f.write(modified_line)
                else:
                    f.write(initial_lines[i])

    return True


def ecrypt_2():
    with open('cover.html', 'r') as cover_file:
        cover_lines = cover_file.readlines()

    with open("mess.txt", "r") as f:
        msg = f.readline().strip()
        chars = list(msg.lower())
        binary_seq = ""
        for i in chars:
            if i in 'abcdef':
                binary_seq = binary_seq + "{0:b}".format(ord(i) - 87)
            else:
                binary_seq = binary_seq + bin(ord(i)).replace("0b11", "")

        if len(binary_seq)!=64:
            print("Wiadomość musi miec 64bity")
            return False
        numofSpaces=0
        emlines=[]
        for i, line in enumerate(cover_lines):
            numofSpaces += line.count(' ')
        if len(binary_seq) > numofSpaces:
            raise ValueError("liczba pojedyńczych spcaji mniejsza niż liczba bitów w wiadomości")
        left=len(binary_seq)-1
        counter=0
        with open("watermark.html", 'w') as output_file:
            for i,line in enumerate(cover_lines):
                line = line.strip()
                line = ' '.join(line.split())
                embLine = ''
                for j,ch in enumerate(line):
                    if ch == ' ' and counter <= left:
                        if j != len(line)-1 and line[j+1] != ' ':
                            if j != 0 and line[j-1] != ' ':
                                if binary_seq[counter] == '1':
                                    embLine += ch
                                else:
                                    embLine += ch+' '
                        counter += 1
                    elif ch == ' ' and counter == left+1:
                        embLine += chr(127)
                        counter += 1
                    else:
                        embLine += ch
                emlines.append(embLine+"\n")
            output_file.writelines(emlines)


    return True


def decrypt_1():
    with open("watermark.html", "r") as f:
        encoded_lines = f.readlines()

    message = ""

    for i in range(0, 64):
        if encoded_lines[i][len(encoded_lines[i]) - 2] == " ":
            message = message + "1"
        else:
            message = message + "0"

    bits = [message[i:i + 4] for i in range(0, len(message), 4)]
    decoded_message = ""
    for i in bits:
        decimal = int(i, 2)
        if decimal < 10:
            decoded_message += str(decimal)
        else:
            decoded_message += chr(ord('a') + decimal - 10)
    with open("detect.txt", "w") as d:
        d.write(decoded_message)

    return True


def decrypt_2():
    mess = ""
    stop = True
    with open("watermark.html", 'r') as cover_file:
        cover_lines = cover_file.readlines()
        for i, line in enumerate(cover_lines):
            if not stop:
                break
            for l in range(len(line)):
                if stop:
                    if line[l] == chr(127):
                        stop = False
                        break
                    elif line[l] == ' ' and line[l + 1] != ' ' and l != len(line) - 1 and l != 0 and line[l - 1] != ' ':
                        mess += "1"
                    elif line[l] == ' ' and line[l + 1] == ' ' and l != len(line) - 1:
                        mess += "0"

        bits = [mess[i:i + 4] for i in range(0, len(mess), 4)]
        decoded_message = ""
        for i in bits:
            decimal = int(i, 2)
            if decimal < 10:
                decoded_message += str(decimal)
            else:
                decoded_message += chr(ord('a') + decimal - 10)
        with open("detect.txt", "w") as d:
            d.write(decoded_message)

    return True


s1 = sys.argv[1]
s2 = sys.argv[2]

todo = False

if s1 in ["-e", "e"]:
    if s2 in ["-1", "1"]:
        todo = ecrypt_1
    elif s2 in ["-2", "2"]:
        todo = ecrypt_2
elif s1 in ["-d", "d"]:
    if s2 in ["-1", "1"]:
        todo = decrypt_1
    elif s2 in ["-2", "2"]:
        todo = decrypt_2

else:
    print("Wrong parameter: {}".format(s1))

if todo():
    print("Done")
else:
    print("ERROR !!!")
