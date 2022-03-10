import turtle
# Allows us to use turtles


def draw_center_square(t, sz):
    """Make turtle t draw a square of size sz in the center."""
    t.penup()
    t.setposition(-sz/2, -sz/2)
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()  # Set up the window and its attributes

wn.bgcolor("lightgreen")

wn.title("Lista 1 Questao 1")

trt = turtle.Turtle()  # Create the turtle
trt.pen(fillcolor='deep pink', pencolor='deep pink', pensize=3)
for i in range(1, 6):
    draw_center_square(trt, 20*i)  # Call the function to draw the square

# Final turtle position
trt.penup()
trt.right(90)
trt.forward(10)
trt.left(90)

wn.mainloop()
