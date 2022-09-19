from art import logo


def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations_dict = {"+": add,
                   "-": subtract,
                   "*": multiply,
                   "/": divide}


def calculator():
    print(logo)

    num1 = float(input("Enter the first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_calculation = True

    while continue_calculation:
        operation_symbol = str(input("Pick an operation: "))
        num2 = float(input("What's the next number: "))
        calculation_function = operations_dict[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result} "
                 f"or type 'n' to exit: ") == "y":
            num1 = result
        else:
            continue_calculation = False
            calculator()


calculator()

