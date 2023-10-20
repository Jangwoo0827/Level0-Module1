import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    p = turtle
    p.speed(2)
    # Ask the user what shape they want to draw and store it in a variable
    o = simpledialog.askstring(title=None, prompt="What shape you want to draw?(triangle or square or circle)")
    # Draw the shape requested by the user using if-elif-else statements
    if o == "triangle":
        p.goto(-100, 0)
        p.forward(200)
        p.right(120)
        p.forward(200)
        p.right(120)
        p.forward(200)
        p.right(120)
    if o == "square":
        p.goto(-100, 0)
        p.forward(200)
        p.right(90)
        p.forward(200)
        p.right(90)
        p.forward(200)
        p.right(90)
        p.forward(200)
        p.right(90)
    if o == "circle":
        p.circle(100)

    # Call the turtle .done() method
    turtle.done
