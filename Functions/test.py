##  https://youtu.be/-nh9rCzPJ20
## VENV (Windows)  https://youtu.be/APOPm01BVrk
## git basics  https://youtu.be/HVsySz-h9r4
## Unit testing   https://youtu.be/6tNS--WetLI
import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('World'))
print(greet('Corey'))




# info = '''Python support these data types: int (integers),\
#  float (floating-point numbers), str (String), bool (boolean of True or False),\
#  and more. Double slash for \\\\comment out.'''
# print(info)
# print("Here is a good test for your first windows python.")
# a = str(input("How old are you?  "))
# aint = int(a)
# print("Wow, you are already", aint)

# def my_sum(lst):
#     """Return the sum of the given list."""
#     sum = 0
#     for item in lst: sum += item
#     return sum

# my_sum(5,)