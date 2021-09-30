from decryption import Decryption
from encryption import Encryption


if __name__ == "__main__":
    while True:
        print("\n\n******** Welcome to Encryption Decryption System 🙋‍♂️🙋‍♂️ ********\n\n")
        print("Choose the Option: ")
        print("1). Encryption")
        print("2). Decryption")
        print("3). To Return\n")

        opt = int(input("Choice 📣: "))

        if opt == 1:
            while True:
                print("\n\n******** Encryption 🔒🔒 ********\n")
                print("Choose the Option: ")
                print("1). String Encryption")
                print("2). File Encryption")
                print("3). To Return Main Menu 📃📃\n")

                n = int(input("Choice 📣: "))
                if n == 1:
                    msg = input("Enter a Message: ")
                    enc = Encryption()
                    encrypted_msg = enc.encryptString(msg)
                    print("\nEncrypted Message 🔒🔒: ", encrypted_msg, "\n\n")
                elif n == 2:
                    enc = Encryption()
                    filePath = input("Enter File Path 📃: ").strip()
                    enc.encryptFile(filePath)
                else:
                    break
        elif opt == 2:
            while True:
                print("\n\n******** Decryption 🔑🔑 ********\n")
                print("Choose the Option: ")
                print("1). String Decryption")
                print("2). File Decryption")
                print("3). To Return Main Menu 📃📃\n")

                n = int(input("Choice 📣: "))
                if n == 1:
                    msg = input("Enter a encrypted Message: ")
                    dec = Decryption()
                    decrypted_msg = dec.decryptString(msg)
                    print("\nDecrypted Message 🔑🔑: ", decrypted_msg, "\n\n")
                elif n == 2:
                    dec = Decryption()
                    filePath = input("Enter File Path 📃: ").strip()
                    dec.decryptFile(filePath)
                else:
                    break
        else:
            break
