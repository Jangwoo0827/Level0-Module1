"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import messagebox, simpledialog, Tk
window = Tk()

one = simpledialog.askinteger(title=None, prompt="What is your first number?")
two = simpledialog.askinteger(title=None, prompt="What is your second number?")

sum = 0
sum = one + two

messagebox.showinfo(title=None, message="Sum of your number is " + str(sum))
