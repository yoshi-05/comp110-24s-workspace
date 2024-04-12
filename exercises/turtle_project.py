"""Depiction of an Archery Target with Hit Points!"""
 
__author__ = "730671788"
 
from turtle import Turtle, colormode, done 
colormode(255)
 
 
def main() -> None:
    """The entrypoint of my scene."""
    main_turt: Turtle = Turtle()
    draw_outer_circle(main_turt, 0, -60)
    draw_first_inner_circle(main_turt, 0, -35)
    draw_second_inner_circle(main_turt, 0, -8.5)
    draw_third_inner_circle(main_turt, -4, 8)
    draw_fourth_inner_circle(main_turt, 3, 22)
    draw_hit(main_turt, 0, 0, 2)
    draw_hit(main_turt, 0, 0, 5)
    done()


def draw_outer_circle(turt: Turtle, x: float, y: float) -> None:
    """Draw a circle for the outer layer of the target!"""
    turt.speed(10000)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color("black", "white")
    turt.begin_fill()
    i: int = 0
    while (i < 120):
        turt.forward(5)
        turt.left(3)
        i = i + 1

    turt.end_fill()


def draw_first_inner_circle(turt: Turtle, x: float, y: float) -> None:
    """Draw the second circle!"""
    turt.speed(10000)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color("black", "black")
    turt.begin_fill()
    i: int = 0
    while (i < 90):
        turt.forward(5)
        turt.left(4)
        i = i + 1

    turt.end_fill()


def draw_second_inner_circle(turt: Turtle, x: float, y: float) -> None:
    """Draw the second circle!"""
    turt.speed(10000)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color("white", (99, 204, 250))
    turt.begin_fill()
    i: int = 0
    while (i < 70):
        turt.forward(4)
        turt.left(5)
        i = i + 1
    turt.end_fill()


def draw_third_inner_circle(turt: Turtle, x: float, y: float) -> None:
    """Draw the third circle!"""
    turt.speed(10000)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color("black", "red")
    turt.begin_fill()
    i: int = 0
    while (i < 63):
        turt.forward(3)
        turt.left(6)
        i = i + 1
    turt.end_fill()


def draw_fourth_inner_circle(turt: Turtle, x: float, y: float) -> None:
    """Draw the fourth circle!"""
    turt.speed(10000)
    turt.hideturtle()
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color("black", "yellow")
    turt.begin_fill()
    i: int = 0
    while (i < 45):
        turt.forward(2)
        turt.left(8)
        i = i + 1
    turt.end_fill()


def draw_hit(turt: Turtle, x: float, y: float, recursion_counter: int) -> None:
    """Draw the hit points!"""
    if recursion_counter == 0:
        return
    else:
        turt.speed(10000)
        turt.hideturtle()
        turt.penup()
        turt.goto(x, y)
        turt.pendown()
        turt.color("green")
        turt.forward(10)
        turt.left(180)
        turt.forward(5)
        turt.right(90)
        turt.forward(5)
        turt.left(180)
        turt.forward(10)
    draw_hit(turt, x + 10, y + 10, recursion_counter - 1)


if __name__ == "__main__":
    main()