from tkinter import Widget, END
import kivy.uix.anchorlayout
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class StackLayoutExample(StackLayout):
    my_text = StringProperty("")
    work = StringProperty("")
    def on_button_delete(self):
        my_text = self.my_text[:-1]
        self.my_text = my_text

    def on_button_clear_all(self):
        self.my_text = ""
        self.work = ""

    def on_button_click0(self):
        self.my_text = self.my_text + "0"

    def on_button_click1(self):
        self.my_text = self.my_text + "1"

    def on_button_click2(self):
        self.my_text = self.my_text + "2"

    def on_button_click3(self):
        self.my_text = self.my_text + "3"

    def on_button_click4(self):
        self.my_text = self.my_text + "4"

    def on_button_click5(self):
        self.my_text = self.my_text + "5"

    def on_button_click6(self):
        self.my_text = self.my_text + "6"

    def on_button_click7(self):
        self.my_text = self.my_text + "7"

    def on_button_click8(self):
        self.my_text = self.my_text + "8"

    def on_button_click9(self):
        self.my_text = self.my_text + "9"

    def on_button_plus(self):
        second_plus = self.my_text.find("+")
        plus = self.my_text.find("+")
        if self.my_text.find("+",second_plus) != -1:
            self.work = self.my_text
            my_text = self.my_text[:plus] + ' ' + self.my_text[plus + 1:]
            numbers = my_text.split()
            result = 0
            for e in numbers:
                result = float(result) + float(e)
                result = str(result)
                self.my_text = result
                self.my_text = self.my_text + "+"
        else:
            self.my_text = self.my_text + "+"

    def on_button_minus(self): #has problems when to comes to negtive numbers
        second_minus = self.my_text.find("-")
        minus = self.my_text.find("-")
        if self.my_text.find("-", second_minus) != -1:
            self.work = self.my_text
            my_text = self.my_text[:minus] + ' ' + self.my_text[minus + 1:]
            numbers = my_text.split()
            result = 0
            for e in numbers:
                if result == 0:
                    result = float(e)
                elif result != 0:
                    result = result - float(e)
                    result = str(result)
                    self.my_text = result
                    self.my_text = self.my_text + "-"
        else:
            self.my_text = self.my_text + "-"

    def on_button_x(self):
        second_x = self.my_text.find("*")
        multiply = self.my_text.find("*")
        if self.my_text.find("*", second_x) != -1:
            self.work = self.my_text
            my_text = self.my_text[:multiply] + ' ' + self.my_text[multiply + 1:]
            numbers = my_text.split()
            result = 1
            for e in numbers:
                result = float(result) * float(e)
                result = str(result)
                self.my_text = result
                self.my_text = self.my_text + "*"
        else:
            self.my_text = self.my_text + "*"


    def on_button_divide(self):
        second_divide = self.my_text.find("/")
        divide = self.my_text.find("/")
        if self.my_text.find("/", second_divide) != -1:
            self.work = self.my_text
            my_text = self.my_text[:divide] + ' ' + self.my_text[divide + 1:]
            numbers = my_text.split()
            result = 1
            for e in numbers:
                if e == "0":
                    self.mytext = "Cannot divide by zero"
                elif numbers[0] == numbers[1]:
                    result = numbers[0]
                    result = str(result)
                    self.my_text = result
                elif e == numbers[0]:
                    result = float(e)
                elif e != numbers[0]:
                    result = result / float(e)
                    result = str(result)
                    self.my_text = result
                    self.my_text = self.my_text + "/"

        else:
            self.my_text = self.my_text + "/"

    def on_button_dec(self):
        self.my_text = self.my_text + "."
    def on_button_equal(self):
        plus = self.my_text.find("+")
        minus = self.my_text.find("-")
        multiply = self.my_text.find("*")
        divide = self.my_text.find("/")
        if plus != -1:
            self.work = self.my_text
            my_text = self.my_text[:plus] + ' ' + self.my_text[plus + 1:]
            numbers = my_text.split()
            result = 0
            for e in numbers:
                result = float(result) + float(e)
                result = str(result)
                self.my_text = result
        elif multiply != -1:
            self.work = self.my_text
            my_text = self.my_text[:multiply] + ' ' + self.my_text[multiply + 1:]
            numbers = my_text.split()
            result = 1
            for e in numbers:
                result = float(result)*float(e)
                result = str(result)
                self.my_text = result
        elif minus != -1:
            self.work = self.my_text
            my_text = self.my_text[:minus] + ' ' + self.my_text[minus + 1:]
            numbers = my_text.split()
            result = 0
            for e in numbers:
                if result == 0:
                    result = float(e)
                elif result != 0:
                    result = result - float(e)
                    result = str(result)
                    self.my_text = result
        elif divide != -1:
            self.work = self.my_text
            my_text = self.my_text[:divide] + ' ' + self.my_text[divide + 1:]
            numbers = my_text.split()
            result = 1
            for e in numbers:
                if e == "0":
                    self.mytext = "Cannot divide by zero"
                elif numbers[0] == numbers[1]:
                    result = numbers[0]
                    result = str(result)
                    self.my_text = result
                elif e == numbers[0]:
                    result = float(e)
                elif e != numbers[0]:
                    result = result/float(e)
                    result = str(result)
                    self.my_text = result


class StackLayoutExample(StackLayout):
    pass


class buttons(App):
    pass


class clicks(App):
    pass


clicks().run()
