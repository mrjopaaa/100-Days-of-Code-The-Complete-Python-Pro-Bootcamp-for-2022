from turtle import Turtle, Screen

joe = Turtle()
joe.speed("fastest")
screen = Screen()
screen.setup(1200, 500)


def move_forwards():
    joe.forward(10)


screen.listen()
screen.onkey(move_forwards, "space")
screen.exitonclick()
