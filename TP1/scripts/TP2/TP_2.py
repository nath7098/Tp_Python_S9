from tkinter import *


def after_result_operation(label, label2):
    if str(label2.cget("text")).endswith('='):
        label2.config(text="")


def AC_function(label, label2):
    after_result_operation(label, label2)
    label.config(text="")
    label2.config(text="")


def C_function(label, label2):
    after_result_operation(label, label2)
    label.config(text="")
    label2.config(text="")


def addition(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "":
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "+")
        label.config(text="")


def multiplication(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "":
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "*")
        label.config(text="")


def division(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "":
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "/")
        label.config(text="")


def substraction(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "":
        label2.config(text=str(label2.cget("text")) + str(label.cget("text"))  + "-")
        label.config(text="")


def equal_function(label, label2):
    after_result_operation(label, label2)
    label2_txt = str(label2.cget("text"))
    if label2_txt.endswith('+') or label2_txt.endswith('-') or label2_txt.endswith('*') or label2_txt.endswith('/'):
        label2.config(text=label2_txt + label.cget("text"))
        label.config(text="")
    label2_txt = str(label2.cget("text"))
    label.config(text=eval(label2_txt))
    label2.config(text=label2.cget("text") + "=")



fenetre = Tk()

buttons_frame = Frame(fenetre)
buttons_frame.grid(row=0, column=0, sticky="ewns")

label = Label(buttons_frame, text="", bg="white", height=2)
label.grid(row=1, columnspan=4, sticky="ewns")
label2 = Label(buttons_frame, text="", bg="white", height=2, fg="#ccc")
label2.grid(row=0, columnspan=4, sticky="ewns")

buttonplus = Button(buttons_frame, text="+", command=lambda: addition(label, label2), relief="raised", width=5,
                    height=3)
buttonplus.grid(row=2, column=3)
buttonminus = Button(buttons_frame, text="-", command=lambda: substraction(label, label2), relief="raised", width=5,
                     height=3)
buttonminus.grid(row=3, column=3)
buttontimes = Button(buttons_frame, text="x", command=lambda: multiplication(label, label2), relief="raised", width=5,
                     height=3)
buttontimes.grid(row=4, column=3)
buttondiv = Button(buttons_frame, text="/", command=lambda: division(label, label2), relief="raised", width=5, height=3)
buttondiv.grid(row=2, column=2)

buttondequals = Button(buttons_frame, text="=", command=lambda: equal_function(label, label2), relief="raised", width=5,
                       height=3)
buttondequals.grid(row=5, column=3)
buttonC = Button(buttons_frame, text="C", command=lambda: C_function(label, label2), relief="raised", width=5, height=3)
buttonC.grid(row=2, column=0)
buttonAC = Button(buttons_frame, text="AC", command=lambda: AC_function(label, label2), relief="raised", width=5,
                  height=3)
buttonAC.grid(row=2, column=1)

button0 = Button(buttons_frame, text="0", command=lambda: label.config(text="0"), relief="raised", width=5, height=3)
button0.grid(row=6, column=1)
button1 = Button(buttons_frame, text="1", command=lambda: label.config(text="1"), relief="raised", width=5, height=3)
button1.grid(row=5, column=0)
button2 = Button(buttons_frame, text="2", command=lambda: label.config(text="2"), relief="raised", width=5, height=3)
button2.grid(row=5, column=1)
button3 = Button(buttons_frame, text="3", command=lambda: label.config(text="3"), relief="raised", width=5, height=3)
button3.grid(row=5, column=2)
button4 = Button(buttons_frame, text="4", command=lambda: label.config(text="4"), relief="raised", width=5, height=3)
button4.grid(row=4, column=0)
button5 = Button(buttons_frame, text="5", command=lambda: label.config(text="5"), relief="raised", width=5, height=3)
button5.grid(row=4, column=1)
button6 = Button(buttons_frame, text="6", command=lambda: label.config(text="6"), relief="raised", width=5, height=3)
button6.grid(row=4, column=2)
button7 = Button(buttons_frame, text="7", command=lambda: label.config(text="7"), relief="raised", width=5, height=3)
button7.grid(row=3, column=0)
button8 = Button(buttons_frame, text="8", command=lambda: label.config(text="8"), relief="raised", width=5, height=3)
button8.grid(row=3, column=1)
button9 = Button(buttons_frame, text="9", command=lambda: label.config(text="9"), relief="raised", width=5, height=3)
button9.grid(row=3, column=2)

fenetre.mainloop()
