#Amir Abdollah Abdollahi
import turtle

def draw_triangle(x0, y0, x1, y1, x2, y2):

    turtle.setworldcoordinates(0, 0, 1, 1)

    turtle.penup()
    turtle.goto(x0, y0)
    turtle.pendown()

    turtle.goto(x1, y1)
    turtle.goto(x2, y2)
    turtle.goto(x0, y0)


draw_triangle(0.2, 0.2, 0.8, 0.2, 0.5, 0.8)

turtle.done()