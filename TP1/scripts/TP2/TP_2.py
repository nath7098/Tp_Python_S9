from tkinter import *


def calc(ca):
    if ca == "0":
        return True



if __name__ == '__main__':

    fenetre = Tk()

    Label(fenetre, text="0", bg="white", width=20, height=5, borderwidth=5, font=2).grid(row=0, column=0, columnspan=5,
                                                                                         sticky="ew")
    for ligne in range(3):
        for colonne in range(3):
            Button(fenetre, text=3 * ligne + colonne + 1, width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=ligne + 2,
                                                                                                          column=colonne)

    button1 = Button(fenetre, text="0", width=20, height=5, borderwidth=5, font=2, command=lambda: print("salut")).grid(
        row=5, column=0, columnspan=3, sticky="ew")
    Button(fenetre, text=",", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=1, column=4)
    Button(fenetre, text="+", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=4, column=4)
    Button(fenetre, text="-", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=3, column=4)
    Button(fenetre, text="*", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=2, column=4)
    Button(fenetre, text="/", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=5, column=4)

    Button(fenetre, text="AC", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=1, column=0)
    Button(fenetre, text="C", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=1, column=1)
    Button(fenetre, text="=", width=20, height=5, borderwidth=5, font=2, command=lambda: calc()).grid(row=1, column=2)

    fenetre.mainloop()
