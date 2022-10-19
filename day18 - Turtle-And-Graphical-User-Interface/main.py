from turtle import Turtle, Screen

joe = Turtle()


def triangle():
    shape_draw(3, "#00FA9A")


def square():
    shape_draw(4, "#DCDCDC")


def pentagon():
    shape_draw(5, "#A52A2A")


def hexagon():
    shape_draw(6, "#556B2F")


def heptagon():
    shape_draw(7, "#DCDCDC")


def octagon():
    shape_draw(8, "#556B2F")


def nonagon():
    shape_draw(9, "#00FA9A")


def decagon():
    shape_draw(10, "#DCDCDC")


def shape_draw(num_sides, color):
    for _ in range(num_sides):
        angel = 360 / num_sides
        joe.color(color)
        joe.forward(100)
        joe.right(angel)


def main():
    triangle()
    square()
    pentagon()
    hexagon()
    heptagon()
    octagon()
    nonagon()
    decagon()


main()

# for _ in range(15):
#     joe.forward(10)
#     joe.penup()
#     joe.forward(10)
#     joe.pendown()


# def drawdot(space, x):
#     for i in range(x):
#         for j in range(x):
#             joe.dot()
#
#             joe.forward(space)
#         joe.backward(space * x)
#
#         joe.right(90)
#         joe.forward(space)
#         joe.left(90)


# drawdot(10, 10)
# drawline(15, 10)


screen = Screen()
screen.exitonclick()
