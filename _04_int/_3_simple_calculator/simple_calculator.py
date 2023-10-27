"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk
window = Tk()

one = simpledialog.askinteger(title=None, prompt="What is your first number?")
two = simpledialog.askinteger(title=None, prompt="What is your second number?")

cal = simpledialog.askstring(title=None, prompt="Choose.(add or subtract or multiply or divide)")

if cal == "add":
    sum = 0
    sum = one + two
    messagebox.showinfo(title=None, message="Sum of your number is " + str(sum))
elif cal == "subtract":
    sub = 0
    sub = one - two
    messagebox.showinfo(title=None, message="Difference of your number is " + str(sub))
elif cal == "multiply":
    mul = 0
    mul = one * two
    messagebox.showinfo(title=None, message="Product of your number is " + str(mul))
elif cal == "divide":
    div = 0
    div = one / two
    messagebox.showinfo(title=None, message="Quotient of your number is " + str(div))
else:
    q = 1
    for i in range(100):
        messagebox.showinfo(title=None, message="Congrats! Nothing here!")
        print(q, "Congrats! Nothing here!")
        q = q + 1
