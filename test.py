import random


def keyGenerator():
    r = ""
    for i in range(0, 6):
        r += str(random.randint(1, 9))
    return r


def encryptFile():
    key = keyGenerator()
    with open("abc.txt", "r") as input:
        with open("output.txt", "w") as output:
            for line in input:
                for c in line:
                    i = ord(c)
                    if i != 13 and i != 32:
                        # 13 for new line.
                        # 32 for space.
                        i = i + int(key[3])
                        if i == 13:
                            i = i - int(key[3])

                    output.write(chr(i))

    output.close()
    input.close()
    print("Key Is: ", key)
    print("Encrypted File is at: ", output.name)


def decryptFile():
    try:
        key = input("Enter a key: ")
        with open("output.txt", "r") as inp:
            with open("abc.txt", "w") as output:
                for line in inp:
                    for c in line:
                        i = ord(c)
                        if i != 13 and i != 32:
                            # 13 for new line.
                            # 32 for space.
                            i = i - int(key[3])
                            if i == 13:
                                i = i + int(key[3])

                        output.write(chr(i))
        output.close()
        inp.close()
        print("Decrypted File is at: ", output.name)
    except Exception as e:
        print(e)


# encryptFile()
decryptFile()
