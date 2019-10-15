from tkinter import *
from re import *
from math import sqrt, cos, sin, tan

STANDARD_MODE = 0
SCIENTIFIC_MODE = 1


class MyCalculator(Tk):
    currentmode = STANDARD_MODE

    def __init__(self):
        Tk.__init__(self)
        self.buttons_frame = Frame(self)
        self.menubar = Menu(self)
        self.config(menu=self.menubar)
        self.modemenu = Menu(self.menubar)
        self.modemenu.add_command(label="Standard", command=lambda: self.set_standard_mode())
        self.modemenu.add_command(label="Scientific", command=lambda: self.set_scientific_mode())
        self.menubar.add_cascade(label="Mode", menu=self.modemenu)
        self.label = Label(self.buttons_frame, text="", bg="white", height=2)
        self.label2 = Label(self.buttons_frame, text="", bg="white", height=2, fg="#ccc")
        self.buttonplus = Button(self.buttons_frame, text="+", command=lambda: self.addition(), relief="raised",
                                 width=5, height=3)
        self.buttonminus = Button(self.buttons_frame, text="-", command=lambda: self.substraction(), relief="raised",
                                  width=5, height=3)
        self.buttontimes = Button(self.buttons_frame, text="x", command=lambda: self.multiplication(), relief="raised",
                                  width=5, height=3)
        self.buttondiv = Button(self.buttons_frame, text="/", command=lambda: self.division(), relief="raised", width=5,
                                height=3)
        self.buttondequals = Button(self.buttons_frame, text="=", command=lambda: self.equal_function(),
                                    relief="raised",
                                    width=5, height=3)
        self.buttonC = Button(self.buttons_frame, text="C", command=lambda: self.C_function(), relief="raised", width=5,
                              height=3)
        self.buttonAC = Button(self.buttons_frame, text="AC", command=lambda: self.AC_function(), relief="raised",
                               width=5, height=3)
        self.buttonsign = Button(self.buttons_frame, text="+/-", command=lambda: self.sign_function(), relief="raised",
                                 width=5, height=3)
        self.button0 = Button(self.buttons_frame, text="0", command=lambda: self.input_number("0"), relief="raised",
                              width=5, height=3)
        self.button1 = Button(self.buttons_frame, text="1", command=lambda: self.input_number("1"), relief="raised",
                              width=5, height=3)
        self.button2 = Button(self.buttons_frame, text="2", command=lambda: self.input_number("2"), relief="raised",
                              width=5, height=3)
        self.button3 = Button(self.buttons_frame, text="3", command=lambda: self.input_number("3"), relief="raised",
                              width=5, height=3)
        self.button4 = Button(self.buttons_frame, text="4", command=lambda: self.input_number("4"), relief="raised",
                              width=5, height=3)
        self.button5 = Button(self.buttons_frame, text="5", command=lambda: self.input_number("5"), relief="raised",
                              width=5, height=3)
        self.button6 = Button(self.buttons_frame, text="6", command=lambda: self.input_number("6"), relief="raised",
                              width=5, height=3)
        self.button7 = Button(self.buttons_frame, text="7", command=lambda: self.input_number("7"), relief="raised",
                              width=5, height=3)
        self.button8 = Button(self.buttons_frame, text="8", command=lambda: self.input_number("8"), relief="raised",
                              width=5, height=3)
        self.button9 = Button(self.buttons_frame, text="9", command=lambda: self.input_number("9"), relief="raised",
                              width=5, height=3)
        self.buttonrpar = Button(self.buttons_frame, text=")", command=lambda: self.input_number(")"), relief="raised",
                                 width=5, height=3)
        self.buttonlpar = Button(self.buttons_frame, text="(", command=lambda: self.input_number("(", ),
                                 relief="raised",
                                 width=5, height=3)
        self.buttonpower = Button(self.buttons_frame, text="pow", command=lambda: self.power(), relief="raised",
                                  width=5, height=3)
        self.buttoncos = Button(self.buttons_frame, text="cos", command=lambda: self.cos_function(), relief="raised",
                                width=5, height=3)
        self.set_standard_mode()

    def set_scientific_mode(self):
        current_mode = SCIENTIFIC_MODE
        self.buttons_frame.forget()
        self.buttons_frame.grid(row=0, column=0, sticky="ewns")
        self.label.grid(row=1, columnspan=5, sticky="ewns")
        self.label2.grid(row=0, columnspan=5, sticky="ewns")
        self.buttonplus.grid(row=2, column=3)
        self.buttonminus.grid(row=3, column=3)
        self.buttontimes.grid(row=4, column=3)
        self.buttondiv.grid(row=2, column=2)
        self.buttondequals.grid(row=5, column=3)
        self.buttonsign.grid(row=6, column=0)
        self.button0.grid(row=6, column=1)
        self.button1.grid(row=5, column=0)
        self.button2.grid(row=5, column=1)
        self.button3.grid(row=5, column=2)
        self.button4.grid(row=4, column=0)
        self.button5.grid(row=4, column=1)
        self.button6.grid(row=4, column=2)
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)
        self.buttonC.grid(row=2, column=0)
        self.buttonAC.grid(row=2, column=1)
        self.buttonrpar.grid(row=3, column=4)
        self.buttonlpar.grid(row=2, column=4)
        self.buttonpower.grid(row=4, column=4)
        self.buttoncos.grid(row=5, column=4)

    def set_standard_mode(self):
        current_mode = STANDARD_MODE
        self.buttonrpar.grid_forget()
        self.buttonlpar.grid_forget()
        self.buttonpower.grid_forget()
        self.buttoncos.grid_forget()
        self.buttons_frame.forget()
        self.buttons_frame.grid(row=0, column=0, sticky="ewns")
        self.label.grid(row=1, columnspan=4, sticky="ewns")
        self.label2.grid(row=0, columnspan=4, sticky="ewns")
        self.buttonplus.grid(row=2, column=3)
        self.buttonminus.grid(row=3, column=3)
        self.buttontimes.grid(row=4, column=3)
        self.buttondiv.grid(row=2, column=2)
        self.buttondequals.grid(row=5, column=3)
        self.buttonsign.grid(row=6, column=0)
        self.button0.grid(row=6, column=1)
        self.button1.grid(row=5, column=0)
        self.button2.grid(row=5, column=1)
        self.button3.grid(row=5, column=2)
        self.button4.grid(row=4, column=0)
        self.button5.grid(row=4, column=1)
        self.button6.grid(row=4, column=2)
        self.button7.grid(row=3, column=0)
        self.button8.grid(row=3, column=1)
        self.button9.grid(row=3, column=2)
        self.buttonC.grid(row=2, column=0)
        self.buttonAC.grid(row=2, column=1)

    def input_number(self, num):
        self.label.config(text=str(self.label.cget("text")) + num)

    def sign_function(self):
        regexall = r"(\d+$|\(\-\d+\)|^\-\d+)$"
        regexminus = r"(\(\-\d+\)|^\-\d+)"
        regexendsign = r"(\d+|\(\-\d+\)|^\-\d+)[\-\+\*\/\=]$"

        lab = str(self.label.cget("text"))
        lab2 = str(self.label2.cget("text"))
        self.label2.config(text=lab2 + lab)
        self.label.config(text="")
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
        self.label2.config(text=lab2)
        if lab2.endswith("="):
            self.label.config(text=str(eval(lab2)[:len(lab2) - 1]))
        else:
            self.label.config(text=str(eval(lab2)))

    def equal_function(self):
        self.after_result_operation()
        label2_txt = str(self.label2.cget("text"))
        if self.number_and_endswithsymbol():
            self.label2.config(text=label2_txt + self.label.cget("text"))
            self.label.config(text="")
            label2_txt = str(self.label2.cget("text"))
            self.label.config(text=eval(label2_txt))

    def substraction(self):
        self.after_result_operation()
        if self.label.cget("text") != "" or not self.nonumber_and_endswithsymbol():
            self.label2.config(text=str(self.label2.cget("text")) + str(self.label.cget("text")) + "-")
            self.label.config(text="")

    def after_result_operation(self):
        if str(self.label2.cget("text")).endswith('='):
            self.label2.config(text="")

    def nonumber_and_endswithsymbol(self):
        regex = "[\+\-\*\/\=]"
        lab = str(self.label.cget("text"))
        lab2 = str(self.label2.cget("text"))
        length = len(lab2)
        if lab == "" and search(regex, str(lab2)[length - 1: length]):
            return TRUE
        elif lab == "" and not search(regex, str(lab2)[length - 1: length]):
            return FALSE

    def number_and_endswithsymbol(self):
        regex = "[\+\-\*\/\=]"
        lab = str(self.label.cget("text"))
        lab2 = str(self.label2.cget("text"))
        length = len(lab2)
        if lab != "" and search(regex, str(lab2)[length - 1: length]):
            return TRUE
        elif lab != "" and not search(regex, str(lab2)[length - 1: length]):
            return FALSE

    def AC_function(self):
        self.after_result_operation()
        self.label.config(text="")
        self.label2.config(text="")

    def C_function(self):
        self.after_result_operation()
        self.label.config(text="")

    def cos_function(self):
        self.after_result_operation()
        label2_txt = str(self.label2.cget("text"))
        if self.nonumber_and_endswithsymbol():
            self.label2.config(text="cos(" + label2_txt + self.label.cget("text") + ")")
            self.label.config(text="")
            label2_txt = str(self.label2.cget("text"))
            self.label.config(text=eval(label2_txt))
        elif label2_txt == "" and str(self.label.cget("text")) != "":
            self.label2.config(text="cos(" + self.label.cget("text") + ")")
            self.label.config(text="")
            label2_txt = str(self.label2.cget("text"))
            self.label.config(text=eval(label2_txt))

    def addition(self):
        self.after_result_operation()
        if self.label.cget("text") != "" or not self.nonumber_and_endswithsymbol():
            self.label2.config(text=str(self.label2.cget("text")) + str(self.label.cget("text")) + "+")
            self.label.config(text="")

    def multiplication(self):
        self.after_result_operation()
        if self.label.cget("text") != "" or not self.nonumber_and_endswithsymbol():
            self.label2.config(text=str(self.label2.cget("text")) + str(self.label.cget("text")) + "*")
            self.label.config(text="")

    def power(self):
        self.after_result_operation()
        if self.label.cget("text") != "" or not self.nonumber_and_endswithsymbol():
            self.label2.config(text=str(self.label2.cget("text")) + str(self.label.cget("text")) + "**")
            self.label.config(text="")

    def division(self):
        self.after_result_operation()
        if self.label.cget("text") != "" or not self.nonumber_and_endswithsymbol():
            self.label2.config(text=str(self.label2.cget("text")) + str(self.label.cget("text")) + "/")
            self.label.config(text="")
