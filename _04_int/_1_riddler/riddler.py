

"""
* Write a python program that asks the user a minimum of 3 riddles.
* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer.

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()

one = simpledialog.askstring(title=None, prompt="If 1=5, 2=15, 3=215, and 4=3215. What does 5 equal?")
two = simpledialog.askstring(title=None, prompt="Only one color, but not one size, Stuck at the bottom, yet easily flies. Present in sun, but not in rain, Doing no harm, and feeling no pain. What is it?")
three = simpledialog.askstring(title=None, prompt="Before Mount Everest was discovered, what was the highest mountain on Earth?")
score = 0
if one == "1":
    score = score + 1
if two == "shadow":
    score = score + 1
if three == "mount everest":
    score = score + 1

if score == 1:
    messagebox.showinfo(title=None, message= "Your score is 1!")
if score == 2:
    messagebox.showinfo(title=None, message= "Your score is 2!")
if score == 3:
    messagebox.showinfo(title=None, message= "Your score is 3!")
