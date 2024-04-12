from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.speed(100)
leo.hideturtle()

leo.penup()
leo.goto(-150, -60)
leo.pendown()
leo.color("black", "white")

leo.begin_fill()

side_length: int = 5
i: int = 0
while (i < 120):
    leo.forward(5)
    leo.left(3)
    i = i + 1

leo.end_fill()


done()