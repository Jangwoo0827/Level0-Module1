# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

# Area = πr^2
# Circumference = 2πr
import turtle
from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    r = simpledialog.askinteger(title=None, prompt="How many pixels are in the radius?")
    q = turtle.Turtle()
    q.speed(123)
    q.circle(r)
    q.penup()
    q.goto(0.5, 0.1)
    t = simpledialog.askstring(title=None, prompt="Choose.(Area or circumference)")
    if t == "area":
        w = math.pi*(r**2)
        q.goto(-100, 0.5)
        q.right(90)
        q.forward(100)
        q.write(arg="area =" + str(w), move=True, align='left', font=('Arial', 20, 'normal'))
        q.hideturtle()
    if t == "circumference":
        w = 2*(math.pi)*r
        q.goto(-150, 0.5)
        q.right(90)
        q.forward(100)
        q.write(arg="circumference =" + str(w), move=True, align='left', font=('Arial', 20, 'normal'))
        q.hideturtle()
    turtle.done()


