from utils import create_matrix, make_key, keyGenerator


class Encryption:
    def encryptString(self, msg):

        msg = msg.replace(" ", "")

        C = make_key()

        len_check = len(msg) % 2 == 0
        if not len_check:
            msg += "0"

        P = create_matrix(msg)

        msg_len = int(len(msg) / 2)

        encrypted_msg = ""
        for i in range(msg_len):
            row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]

            integer = int(row_0 % 26 + 65)

            encrypted_msg += chr(integer)

            row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
            integer = int(row_1 % 26 + 65)
            encrypted_msg += chr(integer)
        return encrypted_msg

    def encryptFile(self, file):
        try:
            key = keyGenerator()
            with open(file, "r") as input:
                with open("encrypted.txt", "w") as output:
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
            print("Key is 🔑🔑 :", key)
            print("\nEncrypted File is at 📃🔒:", output.name)
        except Exception as e:
            print("Error:", e)
