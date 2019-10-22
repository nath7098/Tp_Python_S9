from tkinter import *
import hashlib,base64
from Cryptodome.Cipher import AES
from Cryptodome import Random


#Page de connexion
def registrationWindow():
    label_login = Label(window, text="Login : ", height=2)
    label_login.pack()
    input_login = Entry(window, bd=5)
    input_login.pack()
    label_password = Label(window, text="PassWord :", height=2)
    label_password.pack()
    input_password = Entry(window, show="*", bd=5)
    input_password.pack()
    button_register = Button(window, text="Register", height=2,
                             command=lambda: register(input_login.get(), input_password.get()))
    button_register.pack()
    button_login = Button(window, text="Log in", height=2,
                          command=lambda: logIn(input_login.get(), input_password.get()))
    button_login.pack()
    button_exit = Button(window, text="Exit", height=2,
                          command=lambda: exit())
    button_exit.pack()
    window.mainloop()

#Page encrypting and decrypting
def mainWindow():
    main_window = Tk()

    label_file = Label(main_window, text="File Name : ", height=2)
    label_file.pack()
    input_file = Entry(main_window, bd=5)
    input_file.pack()
    button_encrypt = Button(main_window, text="Encrypt", height=2, command=lambda: encryptFile(input_file.get()))
    button_encrypt.pack()
    button_decrypt = Button(main_window, text="Decrypt", height=2, command=lambda: decryptFile(input_file.get()))
    button_decrypt.pack()
    button_exit = Button(main_window, text="Log out", height=2, command=lambda: exit())
    button_exit.pack()

    main_window.mainloop()

#Register in file txt
def register(login,password):
    print(login,password)
    password = password.strip()+login.strip()+"strong"
    hash_password = hashlib.sha512(password.encode()).hexdigest()
    object_file = open("AccountFile.txt", "a")
    text = login+";"+hash_password+";"+"strong\n"
    object_file.write(text)
    object_file.close()
    print(hash_password)

#Check file txt and if it's ok you can go to the next page for encrypting file
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
                window.destroy()
                mainWindow()
                print("Success")

    object_file.close()

# Salage : https://fr.wikipedia.org/wiki/Salage_%28cryptographie%29

# For cutting bloc on same blocs
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
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(enc[16:])

#Encrypte File with static key
def encryptFile(file_name):
    try :
        object_file1 = open(file_name,"rb")
        object_file2 = open("encrypted_"+file_name.strip(),"wb")
        line_file = object_file1.read()
        cipher = AESCipher("vincentpozzicode")
        crypt_line = cipher.encrypt(line_file)
        object_file2.write(crypt_line)

        object_file1.close()
        object_file2.close()
    except FileNotFoundError:
        toplevel = Toplevel()
        label_error = Label(toplevel, text="Le fichier est introuvable", height=0, width=100)
        label_error.pack()

#Decrypt file with static key
def decryptFile(file_name):
    try :

        object_file1 = open("encrypted_"+file_name.strip(), "r")

        object_file2 = open("decrypted_"+file_name.strip(), "w")
        line_file = object_file1.read()
        cipher = AESCipher("vincentpozzicode")
        crypt_line = cipher.decrypt(line_file)
        object_file2.write(crypt_line.decode("utf8"))

        object_file1.close()
        object_file2.close()

    except FileNotFoundError:
        toplevel = Toplevel()
        label_error = Label(toplevel, text="Le fichier est introuvable", height=0, width=100)
        label_error.pack()

#Main
if __name__ == '__main__':
    window = Tk()
    registrationWindow()