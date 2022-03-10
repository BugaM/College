import turtle
# Allows us to use turtles


def draw_poly(t, n, sz):
    """ MAke turtle t draw a polygon of n sides and size sz"""
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


if __name__ == '__main__':  # main function for testing
    wn = turtle.Screen()  # Set up the window and its attributes

    wn.bgcolor("lightgreen")

    wn.title("Lista 1 Questao 2")

    tess = turtle.Turtle()  # Create the turtle
    tess.pen(fillcolor='deep pink', pencolor='deep pink', pensize=3)
    draw_poly(tess, 8, 50)

    wn.mainloop()
