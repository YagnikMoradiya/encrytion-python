class Encryption:
    message = input("Enter a string: ")
    key = input("Enter a key: ")

    # Here i made 3 * 3 list with 0 value
    keyMatrix = [[0] * 3 for i in range(3)]

    # 1 * 3 list for message matrix
    msgMatrix = [[0] for i in range(3)]

    cipMatrix = [[0] for i in range(len(message))]

    cipherText = []

    def fun(self):
        while len(self.message) % 3 != 0:
            self.message += 'x'

        while len(self.key) != 9:
            if len(self.key) > 9:
                self.key -= 'x'
            else:
                self.key += 'x'

        self.hillCifer(self.message, self.key)

        print("Ciphertext: ", "".join(self.cipherText))

    def hillCifer(self, message, key):
        if len(key) < 6 or len(message.strip()) == 0:
            return

        # To get a keyMatrix
        self.getKeyMatrix(key)

        # Fill the data of msgMatrix
        for i in range(0, len(message), 3):
            for j in range(3):
                self.msgMatrix[j][0] = ord(message[j+i]) % 65

            # Encrypt the text and store into cipMatrix
            self.encryptText(self.msgMatrix)

            # Get the text from cipMatrix and push into cipherText
            for i in range(len(self.msgMatrix)):
                self.cipherText.append(chr(self.cipMatrix[i][0] + 65))

    def getKeyMatrix(self, key):
        x = 0
        for i in range(3):
            for j in range(3):
                self.keyMatrix[i][j] = ord(key[x]) % 65
                x += 1

    def encryptText(self, vector):
        for i in range(3):
            for j in range(1):
                self.cipMatrix[i][j] = 0
                for k in range(3):
                    self.cipMatrix[i][j] += (vector[k]
                                             [j] * self.keyMatrix[i][k])
                    self.cipMatrix[i][j] = self.cipMatrix[i][j] % 26


encryption = Encryption()

encryption.fun()
