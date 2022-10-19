import turtle as t
import random

t.colormode(255)
joe = t.Turtle()
joe.speed("fastest")
joe.penup()
joe.hideturtle()

color_list = [(230, 227, 227), (229, 223, 223), (217, 227, 227), (195, 172, 172), (222, 227, 227), (157, 97, 97),
              (185, 159, 159), (9, 53, 53), (125, 37, 37), (55, 33, 33), (110, 69, 69), (118, 162, 162), (27, 118, 118),
              (74, 35, 35), (85, 138, 138), (10, 62, 62), (71, 153, 153), (121, 35, 35), (182, 98, 98), (207, 202, 202),
              (144, 176, 176), (178, 150, 150), (176, 202, 202), (217, 179, 179), (22, 77, 77), (33, 79, 79),
              (95, 143, 143), (160, 111, 111), (214, 178, 178), (168, 202, 202)]

joe.setheading(225)
joe.forward(300)
joe.setheading(0)
number_of_dots = 100


def draw():
    for dot_count in range(1, number_of_dots + 1):
        joe.dot(20, random.choice(color_list))
        joe.forward(50)

        if dot_count % 10 == 0:
            joe.setheading(90)
            joe.forward(50)
            joe.setheading(180)
            joe.forward(500)
            joe.setheading(0)


draw()

screen = t.Screen()
screen.exitonclick()
