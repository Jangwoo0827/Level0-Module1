import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    p = turtle.Turtle()
    p.speed(2)
    # Ask the user what shape they want to draw and store it in a variable
    o = simpledialog.askstring(title=None, prompt="What shape you want to draw?(triangle or square or circle)")
    # Draw the shape requested by the user using if-elif-else statements
    if o == "triangle":
        for i in range(3):
            p.forward(100)
            p.right(120)
    if o == "square":
        for i in range(4):
            p.forward(100)
            p.right(90)
    if o == "circle":
        p.circle(60)

    # Call the turtle .done() method
    turtle.done()
