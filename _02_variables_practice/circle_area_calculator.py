import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    r = simpledialog.askinteger(title=None,prompt="How many pixels are in the radius?")
    
    # Make a new turtle
    q = turtle.Turtle()
    q.speed(0)
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    q.circle(r)
    # Call the turtle .penup() method
    q.penup()
    # Move your turtle to a new x,y position using .goto()
    q.goto(0.5, 0.5)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    w = math.pi*(r**2)
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    q.goto(-100, 0.5)
    q.right(90)
    q.forward(100)
    q.write(arg="area =" + str(w), move=True, align='left', font=('Arial', 20, 'normal'))
    # Hide your turtle
    q.hideturtle()
    # Call turtle.done()
    turtle.done()
