from utils import create_matrix_of_integers_from_string, find_multiplicative_inverse, make_key


class Decryption:
    def decryptString(self, encrypted_msg):

        C = make_key()

        # Inverse matrix
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        multiplicative_inverse = find_multiplicative_inverse(determinant)
        C_inverse = C
        # Swap a <-> d
        C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
        # Replace
        C[0][1] *= -1
        C[1][0] *= -1
        for row in range(2):
            for column in range(2):
                C_inverse[row][column] *= multiplicative_inverse
                C_inverse[row][column] = C_inverse[row][column] % 26

        P = create_matrix_of_integers_from_string(encrypted_msg)
        msg_len = int(len(encrypted_msg) / 2)
        decrypted_msg = ""
        for i in range(msg_len):
            column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]

            integer = int(column_0 % 26 + 65)

            decrypted_msg += chr(integer)

            column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
            integer = int(column_1 % 26 + 65)
            decrypted_msg += chr(integer)
        if decrypted_msg[-1] == "0":
            decrypted_msg = decrypted_msg[:-1]
        return decrypted_msg

    def decryptFile(self, file):
        try:
            key = input("Enter a key 🔑🔑 : ").strip()
            with open(file, "r") as inpt:
                with open("decrypted.txt", "w") as output:
                    for line in inpt:
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
            inpt.close()
            print("\nDecrypted File is at 🔑📃:", output.name)
        except Exception as e:
            print(e)
