import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money_for_calculation = 0
profit = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def add_profit(money):
    global profit
    profit += money
    return profit


def calculate_money(quarters, dimes, nickles, pennies):
    quarters = quarters * 0.25
    dimes = dimes * 0.1
    nickles = nickles * 0.05
    pennies = pennies * 0.01
    global money_for_calculation
    money_for_calculation = quarters + dimes + nickles + pennies


def handle_payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    calculate_money(quarters, dimes, nickles, pennies)


def make_coffee(choice, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


def check_resource(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] < resources[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}")
            return False


is_off = False

while not is_off:
    user_input = input(str("What would you like? (espresso/latte/cappuccino): "))
    if user_input == "off":
        print("Turning off machine...")
        time.sleep(1)
        is_off = True
    elif user_input == "report":
        print(f"Water status: {resources.get('water')} ml")
        print(f"Milk status: {resources.get('milk')} ml")
        print(f"Coffee status: {resources.get('coffee')} g")
        print(f"Money: ${profit}")
    else:
        drink_ingredients = MENU[user_input]
        if check_resource(drink_ingredients["ingredients"]):
            handle_payment()
            if money_for_calculation >= drink_ingredients["cost"]:
                change_money = round(money_for_calculation - drink_ingredients["cost"],2)
                make_coffee(user_input, drink_ingredients["ingredients"])
                print(f"Here is ${change_money} dollars in change")
                money_for_calculation = round(money_for_calculation - change_money, 2)
                add_profit(money_for_calculation)
            else:
                print("Sorry that's not enough money. Money refunded.")