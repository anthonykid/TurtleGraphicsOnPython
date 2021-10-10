import turtle

t = turtle.Turtle()

turtle.bgcolor("navy")
turtle.pensize(5)
turtle.speed(30)

while (True):
    for i in range(6):
        for colors in["red", "blue", "pink", "green", "yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.right(10)

        turtle.hideturtle()
    turtle.mainloop()
