import turtle

def draw_square(some_man):
    for i in range(1,5):
        some_man.forward(-100)
        some_man.right(90)

def draw_project():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle first- draws square
    first = turtle.Turtle()
    first.shape("arrow")
    first.color("yellow")
    first.speed(13)
    for i in range(1,73):
        draw_square(first)
        first.right(5)
    #second = turtle.Turtle()
    #second.shape("arrow")
    #second.color("green")
    #second.circle(100)

    window.exitonclick()

draw_project()
