import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    #Draw a square on a red background

    brad = turtle.Turtle()
    brad.speed(3)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_square()
