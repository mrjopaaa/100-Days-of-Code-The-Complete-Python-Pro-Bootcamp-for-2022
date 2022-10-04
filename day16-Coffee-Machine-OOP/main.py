# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("red", "yellow")
# timmy.forward(100)
#
# print(timmy)
#
# screen = Screen()
# print(screen.canvwidth)
# screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.align("l")
# table.add_column("Pokemon name", ["Pikachu", "Squirtel", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = 'l' #change the attribute values of an object
# print(table)


# How to use object:
# e.g: car.speed

# How to call the method:
# e.g: car.stop()

# create objects from blueprint classes:
# e.g: car = CarBluePrint()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_off = False

while not is_off:
    user_input = input(str("What would you like? (espresso/latte/cappuccino): "))
    if user_input == "off":
        print("Turning off machine...")
        is_off = True
    if user_input == "report":
        coffee_maker = CoffeeMaker()
        print(coffee_maker.report())
        money_machine = MoneyMachine()
        money_machine.report()
        # print(f"Money: ${MoneyMachine.report()}")
    else:
        menu = Menu()
        process_payment = MoneyMachine()
        make_coffee = CoffeeMaker()
        if menu.find_drink(order_name=user_input):
            if process_payment.make_payment(menu.find_drink(order_name=user_input).cost):
                if make_coffee.is_resource_sufficient(menu.find_drink(order_name=user_input)):
                    make_coffee.make_coffee(menu.find_drink(order_name=user_input))

    #         if money_for_calculation >= drink_ingredients["cost"]:
    #             change_money = round(money_for_calculation - drink_ingredients["cost"],2)
    #             make_coffee(user_input, drink_ingredients["ingredients"])
    #             print(f"Here is ${change_money} dollars in change")
    #             money_for_calculation = round(money_for_calculation - change_money, 2)
    #             add_profit(money_for_calculation)
    #         else:
    #             print("Sorry that's not enough money. Money refunded.")
