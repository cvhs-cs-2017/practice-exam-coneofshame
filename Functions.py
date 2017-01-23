"""1. Write a function that will double any integer (n) and return the result"""
def double(number):
    doub = number * 2
    return doub


print(double(6))

"""2.  Write a program that will (1) ask the user for an input value, (2) take
that and double it and  (3) print the result.
Include necessary print statements and address whitespace issues."""
def doubleuser():
    number = int(input('Give me a number: '))
    number = double(number)
    return number

print(doubleuser())
