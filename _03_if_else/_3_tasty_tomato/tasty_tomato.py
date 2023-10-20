from tkinter import *
import tkinter as tk
from tkinter import simpledialog

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choice.
q = simpledialog.askstring(title=None, prompt="What tomato color do you like?(red or orange or yellow or green or blue or purple)")

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if q == "red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if q == "orange":
    canvas.create_oval(75, 200, 400, 450, fill="orange", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="orange", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if q == "yellow":
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if q == "green":
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if q == "blue":
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if q == "purple":
    canvas.create_oval(75, 200, 400, 450, fill="purple", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
