import turtle

def draw_square(t,sz):
    """Make turtle t draw a square of size sz"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes

wn.bgcolor("lightgreen") # Set up background color

wn.title("Exercício 1 Lista 1")

alex = turtle.Turtle() # Create the turtle

alex.color("pink")
alex.pensize(3)
size = 0 # Represents the square size
for i in range(5):
    size+=20
    alex.penup()
    alex.goto(-size/2,-size/2) # Move turtle to new starting point
    alex.pendown()
    draw_square(alex, size) # Call the function to draw the square
size+=20
alex.penup()
alex.goto(-size/2,-size/2) # Move turtle to the end point
wn.mainloop()