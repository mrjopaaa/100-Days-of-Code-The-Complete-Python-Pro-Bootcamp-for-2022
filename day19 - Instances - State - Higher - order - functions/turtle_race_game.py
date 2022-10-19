from turtle import Turtle, Screen
import random

is_race_on = False  # flag needed for while loop
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-80, -50, -20, 10, 40, 70]
list_of_turtles = []


def generate_turtles():
    for turtle_index in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[turtle_index])
        turtle.penup()
        turtle.goto(x=-230, y=positions[turtle_index])
        list_of_turtles.append(turtle)


def race():
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet:
        is_race_on = True
        generate_turtles()
        while is_race_on:
            for turtle in list_of_turtles:
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)
                if turtle.xcor() > 230:
                    turtle_color = turtle.pencolor()
                    is_race_on = False
                    if user_bet == turtle_color:
                        print(f"Congrats! {turtle_color} wins. Your pick was {user_bet}. You won!")
                    else:
                        print(f"You lost! Your pick was {user_bet} color but {turtle_color} color won.")


race()

screen.exitonclick()
