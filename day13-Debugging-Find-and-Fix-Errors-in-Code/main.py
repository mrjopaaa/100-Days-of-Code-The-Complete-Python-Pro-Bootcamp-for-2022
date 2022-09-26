# Exercise 1 - Debugging Odd or Even - SOLUTION: jedan znak jednako je assignment, dva znaka jednako je provjera

#number = int(input("Which number do you want to check: "))

#if number % 2 = 0:
#   print("This is an even number.")
#else:
#    print("This is an odd number")

# Exercise 2 - Debugging Leap year - SOLUTION: TypeError, kod inputa data type je string i solution je samo osigurati
#                                              da Year bude tipa integer

#year = input("Which year do you want to check?")

#if year % 4 == 0:
# if year % 100 == 0:
#    if year % 400 == 0:
#      print("Leap year.")
#    else:
#      print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
#  print("Not leap year.")


# Exercise 3 - Debugging FizzBuzz:

#if number % 3 == 0 or number % 5 == 0:
#    print("FizzBuzz")
#if number % 3 == 0:
#    print("Fizz")
#if number % 5 == 0:
#    print("Buzz")
#else:
#    print([number])

#Solution:

#for number in range(1, 101):
#    if number % 3 == 0 and number % 5 == 0:
#        print("FizzBuzz")
#    elif number % 3 == 0:
#        print("Fizz")
#    elif number % 5 == 0:
#        print("Buzz")
#    else:
#        print([number])
