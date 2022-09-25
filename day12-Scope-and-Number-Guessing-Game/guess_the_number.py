import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_for_lucky_number(number_of_retries, lucky_number):
    if number_of_retries > 0:
        guessed_number = int(input(f"You have {number_of_retries} attempts remaining to guess the number.\n"
                                   "Make a guess: "))
        if guessed_number > 100 or guessed_number < 0:
            print("Out of range! You quited a game!")
            return 0
        elif guessed_number == lucky_number:
            print(f"You got it! The answer was {lucky_number}.")
        elif guessed_number > lucky_number:
            number_of_retries = number_of_retries - 1
            print(f"Too high.\n"
                  "Guess again.\n")
            check_for_lucky_number(number_of_retries, lucky_number)
        elif guessed_number < lucky_number:
            number_of_retries = number_of_retries - 1
            print(f"Too low.\n"
                  "Guess again.\n")
            check_for_lucky_number(number_of_retries, lucky_number)
    else:
        print("You've run out of guesses, you lose.")


def set_difficulty():
    difficulty = str(input("Welcome to the Number Guessing Game!\n"
                           "I'm thinking of a number between 1 and 100\n"
                           "Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Wrong pick!")


def main():
    print(logo)
    lucky_number = random.randint(0, 100)
    print(f"Psst, the number you are trying to find is {lucky_number}.")
    turns = set_difficulty()
    check_for_lucky_number(turns, lucky_number)
    main()


main()
