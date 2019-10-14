from tkinter import *
import hashlib,base64,os
from Cryptodome.Cipher import AES
from Cryptodome import Random

def signIn(login,password):
    print(login,password)
    password = password.strip()+login.strip()+"strong"
    hash_password = hashlib.sha512(password.encode()).hexdigest()
    object_file = open("AccountFile.txt", "a")
    text = login+";"+hash_password+";"+"strong\n"
    object_file.write(text)
    object_file.close()
    print(hash_password)

def logIn(login,password):

    object_file = open("AccountFile.txt", "r")
    found = False

    for line in object_file:
        if found:
            continue

        list = line.split(";")
        if list[0].strip() == login.strip():
            try_password = password.strip()+login.strip()+list[2].strip()
            hash_password = hashlib.sha512(try_password.encode()).hexdigest()
            if hash_password.strip() == list[1].strip():
                found = True
                print("Success")

    object_file.close()

# Salage : https://fr.wikipedia.org/wiki/Salage_%28cryptographie%29


BS = 16
pad = lambda s: s + b"\0" * (AES.block_size - len(s) % AES.block_size)

class AESCipher:

    def __init__( self, key ):
        self.key = bytes(key, 'utf-8')

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        print(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(enc[16:])


def encryptFile(file_name,login):
    object_file1 = open(file_name,"rb")
    object_file2 = open("encrypted.txt","wb")
    line_file = object_file1.read()
    cipher = AESCipher("vincentpozzicaro")
    crypt_line = cipher.encrypt(line_file)
    object_file2.write(crypt_line)

    object_file1.close()
    object_file2.close()

def decryptFile(file_name, login):
    object_file1 = open(file_name, "r")
    object_file2 = open("decrypted.txt", "w")
    line_file = object_file1.read()
    print(line_file)
    cipher = AESCipher("vincentpozzicaro")
    crypt_line = cipher.decrypt(line_file)
    print(crypt_line)
    object_file2.write(crypt_line.decode("utf8"))

    object_file1.close()
    object_file2.close()

if __name__ == '__main__':
    encryptFile("test.txt","vincentpozzicaro")
    decryptFile("encrypted.txt","vincentpozzicaro")

    window = Tk()

    label_login = Label(window, text="Login : ", height=2)
    label_login.pack()
    input_login = Entry(window, bd=5)
    input_login.pack()
    label_password = Label(window, text="PassWord :", height=2)
    label_password.pack()
    input_password = Entry(window, show="*", bd=5)
    input_password.pack()
    button_signin= Button(window, text="Sign in", height=2, command=lambda :signIn(input_login.get(),input_password.get()))
    button_signin.pack()
    button_login = Button(window, text="Log in", height=2, command=lambda :logIn(input_login.get(),input_password.get()))
    button_login.pack()

    window.mainloop()