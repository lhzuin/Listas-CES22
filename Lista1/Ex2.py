import turtle

def draw_poly(t, n, sz):
    """Make turtle t draw a regular polygon of size sz and n sides"""
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen() # Set up the window and its attributes

wn.bgcolor("lightgreen") # Set up background color

wn.title("Exercício 2 Lista 1")
tess = turtle.Turtle() # Create turtle
tess.color("pink")
tess.pensize(3)
draw_poly(tess,8,50)
wn.mainloop()