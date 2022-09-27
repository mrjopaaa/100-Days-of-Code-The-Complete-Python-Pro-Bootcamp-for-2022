from art import logo
import random
from art import vs

from game_data import data

COUNT = 0


def get_random_account():
    """Get data from random account from game_data"""
    return random.choice(data)


def get_followers(followers):
    compare_key = ['follower_count']
    for key in compare_key:
        total_followers_num = followers.get(key)
    return total_followers_num


def increment_count():
    global COUNT
    COUNT += 1


def compare():
    compare_a = get_random_account()
    compare_b = get_random_account()
    print(f"Compare A: {compare_a.get('name')}, {compare_a.get('description')}, from {compare_a.get('country')}")
    print(vs)
    print(f"Against B: {compare_b.get('name')}, {compare_b.get('description')}, from {compare_b.get('country')}")
    followers_a = get_followers(compare_a)
    followers_b = get_followers(compare_b)
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == 'A':
        if followers_a > followers_b:
            increment_count()
            print(f"You're right! Current score: {COUNT}")
            compare()
        else:
            print(f"Sorry, that's wrong. Final score: {COUNT}")
            return 0
    elif answer == 'B':
        if followers_b > followers_a:
            increment_count()
            print(f"You're right! Current score: {COUNT}")
            compare()
        else:
            print(f"Sorry, that's wrong. Final score: {COUNT}")
            return 0
    else:
        print("WARNING! Wrong pick. Restart game.")
        return 0


def main():
    print(logo)
    compare()


main()
