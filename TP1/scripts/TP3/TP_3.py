from tkinter import *
import hashlib

def validation(login,password):
    print(login,password)
    hash_password = hashlib.sha512(password.encode()).hexdigest()
    print(hash_password)


if __name__ == '__main__':
    fenetre = Tk()

    label_login = Label(fenetre, text="Login : ", height=2)
    label_login.pack()
    input_login = Entry(fenetre, bd=5)
    input_login.pack()
    label_password = Label(fenetre, text="PassWord :", height=2)
    label_password.pack()
    input_password = Entry(fenetre, show="*", bd=5)
    input_password.pack()
    button_valid = Button(fenetre, text="Sign in", height=2, command=lambda :validation(input_login.get(),input_password.get()))
    button_valid.pack()

    fenetre.mainloop()