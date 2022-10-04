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

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while not is_off:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        print("Turning off machine...")
        is_off = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

