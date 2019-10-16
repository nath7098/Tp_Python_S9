from tkinter import *
from re import *
from math import sqrt, cos, sin, tan

STANDARD_MODE = 0
SCIENTIFIC_MODE = 1


class MyCalculator(Tk):
    currentmode = STANDARD_MODE
    equal_pushed = False

    def __init__(self):
        Tk.__init__(self)
        self.buttons_frame = Frame(self)
        self.menubar = Menu(self)
        self.config(menu=self.menubar)
        self.modemenu = Menu(self.menubar)
        self.modemenu.add_command(label="Standard", command=lambda: self.set_standard_mode())
        self.modemenu.add_command(label="Scientific", command=lambda: self.set_scientific_mode())
        self.menubar.add_cascade(label="Mode", menu=self.modemenu)
        self.singlePrinter = Label(self.buttons_frame, text="", bg="white", height=2)
        self.statementPrinter = Label(self.buttons_frame, text="", bg="white", height=2, fg="#ccc")
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
        self.buttonC = Button(self.buttons_frame, text="C", command=lambda: self.c_function(), relief="raised", width=5,
                              height=3)
        self.buttonAC = Button(self.buttons_frame, text="AC", command=lambda: self.ac_function(), relief="raised",
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

    def init_grid(self):
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

    def set_scientific_mode(self):
        # current_mode = SCIENTIFIC_MODE
        self.buttons_frame.forget()
        self.buttons_frame.grid(row=0, column=0, sticky="ewns")
        self.singlePrinter.grid(row=1, columnspan=5, sticky="ewns")
        self.statementPrinter.grid(row=0, columnspan=5, sticky="ewns")
        self.init_grid()
        self.buttonrpar.grid(row=3, column=4)
        self.buttonlpar.grid(row=2, column=4)
        self.buttonpower.grid(row=4, column=4)
        self.buttoncos.grid(row=5, column=4)

    def set_standard_mode(self):
        # current_mode = STANDARD_MODE
        self.buttonrpar.grid_forget()
        self.buttonlpar.grid_forget()
        self.buttonpower.grid_forget()
        self.buttoncos.grid_forget()
        self.buttons_frame.forget()
        self.buttons_frame.grid(row=0, column=0, sticky="ewns")
        self.singlePrinter.grid(row=1, columnspan=4, sticky="ewns")
        self.statementPrinter.grid(row=0, columnspan=4, sticky="ewns")
        self.init_grid()

    def reset_equal_pushed(self):
        if self.equal_pushed:
            self.equal_pushed = False

    def sign_function(self):
        # definition des regex
        regex_ends_with_number = r"(\d+$|\(\-\d+\)|^\-\d+)$"
        regex_negative_numbers = r"(\(\-\d+\)|^\-\d+)"
        regex_ends_with_sign = r"(\d+|\(\-\d+\)|^\-\d+)[\-\+\*\/]$"

        single = str(self.singlePrinter.cget("text"))
        statement = str(self.statementPrinter.cget("text"))
        array_ends_with_number = findall(regex_ends_with_number, statement)
        array_ens_with_sign = findall(regex_ends_with_sign, statement)

        # Si on a appuyé sur le boutton égal avant on inverse juste le signe du résutat
        if self.equal_pushed:
            if single.startswith("-"):
                self.singlePrinter.config(text=single[1:])
            else:
                self.singlePrinter.config(text="-" + single)
            self.statementPrinter.config(text=self.singlePrinter.cget("text"))
        else:
            self.statementPrinter.config(text=statement + single)
            self.singlePrinter.config(text="")
            # Si le statement se termine par un nombre
            if len(array_ends_with_number) > 0 and len(array_ens_with_sign) == 0:
                last = len(array_ends_with_number) - 1
                num = str(array_ends_with_number[last])
                # Si le nombre est négatif
                if len(findall(regex_negative_numbers, num)) > 0:
                    startindex = 2
                    endindex = len(num) - 1
                    inverted = num[startindex:endindex]
                else:
                    inverted = str("(-" + num + ")")
                statement = statement.replace(num, inverted, 1)
            # Si le statement se termine par un signe + - * ou /
            elif len(array_ends_with_number) == 0 and len(array_ens_with_sign) > 0:
                last = len(array_ens_with_sign) - 1
                num = str(str(array_ens_with_sign[last]))
                if len(findall(regex_negative_numbers, num)):
                    startindex = 2
                    endindex = len(num) - 1
                    inverted = num[startindex:endindex]
                else:
                    inverted = str("(-" + num + ")")
                statement = statement.replace(num, inverted, 1)
            self.statementPrinter.config(text=statement)
            self.singlePrinter.config(text=str(eval(statement)))

    # Retourne vrai si le statement se termine par un signe et l'afficheur unique est vide
    # Retoune faux si le statement ne se termine pas par un signe et l'afficheur est vide
    # utilisation pour bloquer les input de signes
    def nonumberin_singleprinter_and_statement_endswithsymbol(self) -> bool:
        regex = r"[\+\-\*\/\=]"
        lab = str(self.singlePrinter.cget("text"))
        lab2 = str(self.statementPrinter.cget("text"))
        length = len(lab2)
        if lab == "" and search(regex, str(lab2)[length - 1: length]):
            return TRUE
        elif lab == "" and not search(regex, str(lab2)[length - 1: length]):
            return FALSE

    # Retourne vrai si le statement se termine par un signe et l'afficheur unique n'est pas vide
    # Retourne faux si le statement ne se termine pas par un signe et l'afficheur unique n'est pas vide
    # Utilisation pour la fonction equal_function()
    def numberin_singleprinter_and_statement_endswithsymbol(self) -> bool:
        regex = r"[\+\-\*\/\=]"
        lab = str(self.singlePrinter.cget("text"))
        lab2 = str(self.statementPrinter.cget("text"))
        length = len(lab2)
        if lab != "" and search(regex, str(lab2)[length - 1: length]):
            return TRUE
        elif lab != "" and not search(regex, str(lab2)[length - 1: length]):
            return FALSE

    # Fonction pour le boutton AC
    def ac_function(self):
        self.after_result_operation()
        self.singlePrinter.config(text="")
        self.statementPrinter.config(text="")

    # Fonction pour le boutton C
    def c_function(self):
        self.after_result_operation()
        self.singlePrinter.config(text="")

    # Fonction du Cosinus
    def cos_function(self):
        self.after_result_operation()
        single = str(self.singlePrinter.cget("text"))
        statement = str(self.statementPrinter.cget("text"))

        if self.numberin_singleprinter_and_statement_endswithsymbol():
            self.statementPrinter.config(text=statement + "cos(" + single + ")")
            self.singlePrinter.config(text="")
            statement = str(self.statementPrinter.cget("text"))
            self.singlePrinter.config(text=eval(statement))
        elif self.equal_pushed or (statement == "" and single != ""):
            self.statementPrinter.config(text="cos(" + single + ")")
            self.singlePrinter.config(text="")
            statement = str(self.statementPrinter.cget("text"))
            self.singlePrinter.config(text=eval(statement))

    # Fonction pour l'addition
    def addition(self):
        self.after_result_operation()
        if self.singlePrinter.cget("text") != "" or not self.nonumberin_singleprinter_and_statement_endswithsymbol():
            if self.equal_pushed:
                self.statementPrinter.config(text=str(self.singlePrinter.cget("text")) + "+")
            else:
                self.statementPrinter.config(text=str(self.statementPrinter.cget("text")) +
                                                  str(self.singlePrinter.cget("text")) + "+")
            self.singlePrinter.config(text="")

    # Fonction pour la soustraction
    def substraction(self):
        self.reset_equal_pushed()
        if self.singlePrinter.cget(
                "text") != "" or not self.nonumberin_singleprinter_and_statement_endswithsymbol():
            if self.equal_pushed:
                self.statementPrinter.config(text=str(self.singlePrinter.cget("text")) + "-")
            else:
                self.statementPrinter.config(text=str(self.statementPrinter.cget("text")) +
                                                  str(self.singlePrinter.cget("text")) + "-")
            self.singlePrinter.config(text="")

    # Fonction pour la multiplication
    def multiplication(self):
        self.after_result_operation()
        if self.singlePrinter.cget("text") != "" or not self.nonumberin_singleprinter_and_statement_endswithsymbol():
            if self.equal_pushed:
                self.statementPrinter.config(text=str(self.singlePrinter.cget("text")) + "*")
            else:
                self.statementPrinter.config(text=str(self.statementPrinter.cget("text")) +
                                                  str(self.singlePrinter.cget("text")) + "*")
            self.singlePrinter.config(text="")

    # Fonction pour la puissance
    def power(self):
        self.after_result_operation()
        if self.singlePrinter.cget("text") != "" or not self.nonumberin_singleprinter_and_statement_endswithsymbol():
            if self.equal_pushed:
                self.statementPrinter.config(text=str(self.singlePrinter.cget("text")) + "**")
            else:
                self.statementPrinter.config(text=str(self.statementPrinter.cget("text")) +
                                                  str(self.singlePrinter.cget("text")) + "**")
            self.singlePrinter.config(text="")

    # Fonction pour la division
    def division(self):
        self.after_result_operation()
        if self.singlePrinter.cget("text") != "" or not self.nonumberin_singleprinter_and_statement_endswithsymbol():
            if self.equal_pushed:
                self.statementPrinter.config(text=str(self.singlePrinter.cget("text")) + "/")
            else:
                self.statementPrinter.config(text=str(self.statementPrinter.cget("text")) +
                                                  str(self.singlePrinter.cget("text")) + "/")
            self.singlePrinter.config(text="")

    # Fonction pour le calcul égal
    def equal_function(self):
        self.reset_equal_pushed()
        label2_txt = str(self.statementPrinter.cget("text"))
        if self.numberin_singleprinter_and_statement_endswithsymbol():
            self.statementPrinter.config(text=label2_txt + self.singlePrinter.cget("text"))
            self.singlePrinter.config(text="")
            label2_txt = str(self.statementPrinter.cget("text"))
            self.singlePrinter.config(text=eval(label2_txt))
            self.equal_pushed = True
