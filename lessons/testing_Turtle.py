from turtle import Turtle, colormode, done 
colormode(255)

leo_outer: Turtle = Turtle()

leo_outer.speed(100)
leo_outer.hideturtle()

leo_outer.penup()
leo_outer.goto(0, -60)
leo_outer.pendown()
leo_outer.color("black", "white")

leo_outer.begin_fill()

side_length: int = 5
i: int = 0
while (i < 120):
    leo_outer.forward(5)
    leo_outer.left(3)
    i = i + 1

leo_outer.end_fill()

# Second Target

leo_outer2: Turtle = Turtle()

leo_outer2.speed(100)
leo_outer2.hideturtle()

leo_outer2.penup()
leo_outer2.goto(0, -35)
leo_outer2.pendown()
leo_outer2.color("black", "black")

leo_outer2.begin_fill()

i2: int = 0
while (i2 < 90):
    leo_outer2.forward(5)
    leo_outer2.left(4)
    i2 = i2 + 1

leo_outer2.end_fill()

# Third circle for target

leo_outer3: Turtle = Turtle()
leo_outer3.speed(100)
leo_outer3.hideturtle()

leo_outer3.penup()
leo_outer3.goto(0, -8.5)
leo_outer3.pendown()
leo_outer3.color("white", (99, 204, 250))

leo_outer3.begin_fill()
i3: int = 0
while (i3 < 70):
    leo_outer3.forward(4)
    leo_outer3.left(5)
    i3 = i3 + 1

leo_outer3.end_fill()

#Fourth Circle for Target

leo_outer4: Turtle = Turtle()
leo_outer4.speed(100)
leo_outer4.hideturtle()

leo_outer4.penup()
leo_outer4.goto(0, 8)
leo_outer4.pendown()
leo_outer4.color("black", "red")

leo_outer4.begin_fill()
i4: int = 0
while (i4 < 63):
    leo_outer4.forward(3)
    leo_outer4.left(6)
    i4 = i4 + 1

leo_outer4.end_fill()


# Fifth Circle for Target

leo_outer5: Turtle = Turtle()
leo_outer5.speed(100)
leo_outer5.hideturtle()

leo_outer5.penup()
leo_outer5.goto(0, 23)
leo_outer5.pendown()
leo_outer5.color("black", "yellow")

leo_outer5.begin_fill()
i5: int = 0
while (i5 < 45):
    leo_outer5.forward(2)
    leo_outer5.left(8)
    i5 = i5 + 1

leo_outer5.end_fill()
done()
