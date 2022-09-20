import os
import random
from art import logo


def deal_card():
    """"Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if computer_score == user_score:
        print("The result is draw, computer wins.")
    elif computer_score == 0:
        print("Computer has a blackjack. Comp wins!")
    elif user_score == 0:
        print("User has a blackjack. User wins!")
    elif user_score > 21:
        print("User has over 21. User lost!")
    elif computer_score > 21:
        print("Computer has over 21. Computer lost!")
    elif user_score > computer_score:
        print(f"User has a bigger score {user_score} > {computer_score}, user wins.")
    else:
        print(f"Computer has a bigger score {computer_score} > {user_score}, computer wins")


def main():
    print(logo)
    want_play = str(input("Do you want to play game of Blackjack? Type 'y' or 'n': "))
    if want_play == "y":
        user_cards = []
        computer_cards = []
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        print(f"user_cards:{user_cards} and current score is {user_score}")
        computer_score = calculate_score(computer_cards)
        print(f"computer_cards{computer_cards} current score is {computer_score}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            want_play = input("Type 'y' if you want to draw another card or 'n' if you don't: ")
            if want_play == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"computer_cards{computer_cards} current score is {computer_score}")
    compare(user_score, computer_score)

    print(f"User final score is {user_score}")
    print(f"Computer final score is {computer_score}")

    want_restart_game = input("Do you want to restart game. Type 'y' or 'n': ")
    if want_restart_game == 'y':
        os.system('clear')
        main()


main()
