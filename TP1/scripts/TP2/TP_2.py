from tkinter import *
from re import *
from math import sqrt, cos, sin, tan

COMPACT_MODE = 0
SCIENTIFIC_MODE = 1
CURRENT_MODE = 0


def after_result_operation(label, label2):
    if str(label2.cget("text")).endswith('='):
        label2.config(text="")


def nonumber_and_endswithsymbol(label, label2):
    regex = "[\+\-\*\/\=]"
    lab = str(label.cget("text"))
    lab2 = str(label2.cget("text"))
    length = len(lab2)
    if lab == "" and search(regex, str(lab2)[length - 1: length]):
        return TRUE
    elif lab == "" and not search(regex, str(lab2)[length - 1: length]):
        return FALSE

def number_and_endswithsymbol(label, label2):
    regex = "[\+\-\*\/\=]"
    lab = str(label.cget("text"))
    lab2 = str(label2.cget("text"))
    length = len(lab2)
    if lab != "" and search(regex, str(lab2)[length - 1: length]):
        return TRUE
    elif lab != "" and not search(regex, str(lab2)[length - 1: length]):
        return FALSE

def AC_function(label, label2):
    after_result_operation(label, label2)
    label.config(text="")
    label2.config(text="")


def C_function(label, label2):
    after_result_operation(label, label2)
    label.config(text="")


def cos_function(label, label2):
    after_result_operation(label, label2)
    label2_txt = str(label2.cget("text"))
    if nonumber_and_endswithsymbol(label, label2):
        label2.config(text="cos(" + label2_txt + label.cget("text") + ")")
        label.config(text="")
        label2_txt = str(label2.cget("text"))
        label.config(text=eval(label2_txt))
    elif label2_txt == "" and str(label.cget("text")) != "":
        label2.config(text="cos(" + label.cget("text") + ")")
        label.config(text="")
        label2_txt = str(label2.cget("text"))
        label.config(text=eval(label2_txt))


def addition(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "" or not nonumber_and_endswithsymbol(label, label2):
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "+")
        label.config(text="")


def multiplication(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "" or not nonumber_and_endswithsymbol(label, label2):
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "*")
        label.config(text="")


def power(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "" or not nonumber_and_endswithsymbol(label, label2):
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "**")
        label.config(text="")


def division(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "" or not nonumber_and_endswithsymbol(label, label2):
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "/")
        label.config(text="")


def substraction(label, label2):
    after_result_operation(label, label2)
    if label.cget("text") != "" or not nonumber_and_endswithsymbol(label, label2):
        label2.config(text=str(label2.cget("text")) + str(label.cget("text")) + "-")
        label.config(text="")


def equal_function(label, label2):
    after_result_operation(label, label2)
    label2_txt = str(label2.cget("text"))
    if number_and_endswithsymbol(label, label2):
        label2.config(text=label2_txt + label.cget("text"))
        label.config(text="")
        label2_txt = str(label2.cget("text"))
        label.config(text=eval(label2_txt))


def sign_function(label, label2):
    regexall = r"(\d+$|\(\-\d+\)|^\-\d+)$"
    regexminus = r"(\(\-\d+\)|^\-\d+)"
    regexendsign = r"(\d+|\(\-\d+\)|^\-\d+)[\-\+\*\/\=]$"

    lab = str(label.cget("text"))
    lab2 = str(label2.cget("text"))
    label2.config(text=lab2 + lab)
    label.config(text="")
    arr = findall(regexall, lab2)
    arrsign = findall(regexendsign, lab2)
    if len(arr) > 0 and len(arrsign) == 0:
        last = len(arr) - 1
        num = str(arr[last])
        if len(findall(regexminus, num)) > 0:
            startindex = 2
            endindex = len(num) - 1
            inverted = num[startindex:endindex]
        else:
            inverted = str("(-" + num + ")")
        lab2 = lab2.replace(num, inverted, 1)
    elif len(arr) == 0 and len(arrsign) > 0:
        print(arrsign)
        last = len(arrsign) - 1
        num = str(str(arrsign[last]))
        if len(findall(regexminus, num)):
            startindex = 2
            endindex = len(num) - 1
            inverted = num[startindex:endindex]
        else:
            inverted = str("(-" + num + ")")
        print(num)
        print(inverted)
        lab2 = lab2.replace(num, inverted, 1)
    print(lab2)
    label2.config(text=lab2)
    if lab2.endswith("="):
        label.config(text=str(eval(lab2)[:len(lab2) - 1]))
    else:
        label.config(text=str(eval(lab2)))

def input_number(num, label):
    label.config(text=str(label.cget("text")) + num)


def setmodecompact():
    CURRENT_MODE = COMPACT_MODE
    buttonplus = Button(buttons_frame, text="+", command=lambda: addition(label, label2), relief="raised", width=5,
                        height=3)
    buttonplus.grid(row=2, column=3)
    buttonminus = Button(buttons_frame, text="-", command=lambda: substraction(label, label2), relief="raised", width=5,
                         height=3)
    buttonminus.grid(row=3, column=3)
    buttontimes = Button(buttons_frame, text="x", command=lambda: multiplication(label, label2), relief="raised",
                         width=5,
                         height=3)
    buttontimes.grid(row=4, column=3)
    buttondiv = Button(buttons_frame, text="/", command=lambda: division(label, label2), relief="raised", width=5,
                       height=3)
    buttondiv.grid(row=2, column=2)

    buttondequals = Button(buttons_frame, text="=", command=lambda: equal_function(label, label2), relief="raised",
                           width=5,
                           height=3)
    buttondequals.grid(row=5, column=3)
    buttonC = Button(buttons_frame, text="C", command=lambda: C_function(label, label2), relief="raised", width=5,
                     height=3)
    buttonC.grid(row=2, column=0)
    buttonAC = Button(buttons_frame, text="AC", command=lambda: AC_function(label, label2), relief="raised", width=5,
                      height=3)
    buttonAC.grid(row=2, column=1)

    buttonsign = Button(buttons_frame, text="+/-", command=lambda: sign_function(label, label2), relief="raised",
                        width=5, height=3)
    buttonsign.grid(row=6, column=0)
    button0 = Button(buttons_frame, text="0", command=lambda: input_number("0", label), relief="raised", width=5,
                     height=3)
    button0.grid(row=6, column=1)
    button1 = Button(buttons_frame, text="1", command=lambda: input_number("1", label), relief="raised", width=5,
                     height=3)
    button1.grid(row=5, column=0)
    button2 = Button(buttons_frame, text="2", command=lambda: input_number("2", label), relief="raised", width=5,
                     height=3)
    button2.grid(row=5, column=1)
    button3 = Button(buttons_frame, text="3", command=lambda: input_number("3", label), relief="raised", width=5,
                     height=3)
    button3.grid(row=5, column=2)
    button4 = Button(buttons_frame, text="4", command=lambda: input_number("4", label), relief="raised", width=5,
                     height=3)
    button4.grid(row=4, column=0)
    button5 = Button(buttons_frame, text="5", command=lambda: input_number("5", label), relief="raised", width=5,
                     height=3)
    button5.grid(row=4, column=1)
    button6 = Button(buttons_frame, text="6", command=lambda: input_number("6", label), relief="raised", width=5,
                     height=3)
    button6.grid(row=4, column=2)
    button7 = Button(buttons_frame, text="7", command=lambda: input_number("7", label), relief="raised", width=5,
                     height=3)
    button7.grid(row=3, column=0)
    button8 = Button(buttons_frame, text="8", command=lambda: input_number("8", label), relief="raised", width=5,
                     height=3)
    button8.grid(row=3, column=1)
    button9 = Button(buttons_frame, text="9", command=lambda: input_number("9", label), relief="raised", width=5,
                     height=3)
    button9.grid(row=3, column=2)


def setmodescientific():
    CURRENT_MODE = SCIENTIFIC_MODE
    buttonplus = Button(buttons_frame, text="+", command=lambda: addition(label, label2), relief="raised", width=5,
                        height=3)
    buttonplus.grid(row=2, column=3)
    buttonminus = Button(buttons_frame, text="-", command=lambda: substraction(label, label2), relief="raised", width=5,
                         height=3)
    buttonminus.grid(row=3, column=3)
    buttontimes = Button(buttons_frame, text="x", command=lambda: multiplication(label, label2), relief="raised",
                         width=5,
                         height=3)
    buttontimes.grid(row=4, column=3)
    buttondiv = Button(buttons_frame, text="/", command=lambda: division(label, label2), relief="raised", width=5,
                       height=3)
    buttondiv.grid(row=2, column=2)

    buttondequals = Button(buttons_frame, text="=", command=lambda: equal_function(label, label2), relief="raised",
                           width=5,
                           height=3)
    buttondequals.grid(row=5, column=3)
    buttonC = Button(buttons_frame, text="C", command=lambda: C_function(label, label2), relief="raised", width=5,
                     height=3)
    buttonC.grid(row=2, column=0)
    buttonAC = Button(buttons_frame, text="AC", command=lambda: AC_function(label, label2), relief="raised", width=5,
                      height=3)
    buttonAC.grid(row=2, column=1)

    buttonrpar = Button(buttons_frame, text=")", command=lambda: input_number(")", label), relief="raised",
                        width=5, height=3)
    buttonrpar.grid(row=2, column=4)

    buttonlpar = Button(buttons_frame, text="(", command=lambda: input_number("(", label), relief="raised",
                        width=5, height=3)
    buttonlpar.grid(row=3, column=4)

    buttonpower = Button(buttons_frame, text="pow", command=lambda: power(label, label2), relief="raised",
                        width=5, height=3)
    buttonpower.grid(row=4, column=4)

    buttoncos = Button(buttons_frame, text="cos", command=lambda: cos_function(label, label2), relief="raised",
                       width=5, height=3)
    buttoncos.grid(row=5, column=4)

    buttonsign = Button(buttons_frame, text="+/-", command=lambda: sign_function(label, label2), relief="raised",
                        width=5, height=3)
    buttonsign.grid(row=6, column=0)
    button0 = Button(buttons_frame, text="0", command=lambda: input_number("0", label), relief="raised", width=5,
                     height=3)
    button0.grid(row=6, column=1)
    button1 = Button(buttons_frame, text="1", command=lambda: input_number("1", label), relief="raised", width=5,
                     height=3)
    button1.grid(row=5, column=0)
    button2 = Button(buttons_frame, text="2", command=lambda: input_number("2", label), relief="raised", width=5,
                     height=3)
    button2.grid(row=5, column=1)
    button3 = Button(buttons_frame, text="3", command=lambda: input_number("3", label), relief="raised", width=5,
                     height=3)
    button3.grid(row=5, column=2)
    button4 = Button(buttons_frame, text="4", command=lambda: input_number("4", label), relief="raised", width=5,
                     height=3)
    button4.grid(row=4, column=0)
    button5 = Button(buttons_frame, text="5", command=lambda: input_number("5", label), relief="raised", width=5,
                     height=3)
    button5.grid(row=4, column=1)
    button6 = Button(buttons_frame, text="6", command=lambda: input_number("6", label), relief="raised", width=5,
                     height=3)
    button6.grid(row=4, column=2)
    button7 = Button(buttons_frame, text="7", command=lambda: input_number("7", label), relief="raised", width=5,
                     height=3)
    button7.grid(row=3, column=0)
    button8 = Button(buttons_frame, text="8", command=lambda: input_number("8", label), relief="raised", width=5,
                     height=3)
    button8.grid(row=3, column=1)
    button9 = Button(buttons_frame, text="9", command=lambda: input_number("9", label), relief="raised", width=5,
                     height=3)
    button9.grid(row=3, column=2)

fenetre = Tk()
menubar = Menu(fenetre)
fenetre.config(menu=menubar)

modemenu = Menu(menubar)
modemenu.add_command(label="Compact", command=lambda: setmodecompact())
modemenu.add_command(label="Scientific", command=lambda: setmodescientific())
menubar.add_cascade(label="Mode", menu=modemenu)


buttons_frame = Frame(fenetre)
buttons_frame.grid(row=0, column=0, sticky="ewns")

label = Label(buttons_frame, text="", bg="white", height=2)
label.grid(row=1, columnspan=4, sticky="ewns")
label2 = Label(buttons_frame, text="", bg="white", height=2, fg="#ccc")
label2.grid(row=0, columnspan=4, sticky="ewns")
setmodecompact()

fenetre.mainloop()
