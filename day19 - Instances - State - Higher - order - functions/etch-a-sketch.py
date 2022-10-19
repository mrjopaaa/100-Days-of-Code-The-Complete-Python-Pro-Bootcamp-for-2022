from turtle import Turtle, Screen

joe = Turtle()
joe.speed("fastest")



screen.setup(1200, 500)


def move_forwards():
    joe.forward(10)


def move_backwards():
    joe.backward(10)


def move_counter_clockwise():
    joe.left(10)


def move_clockwise():
    joe.right(10)


def clear_screen():
    joe.clear()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()