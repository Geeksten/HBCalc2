"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
user_input = raw_input("> ")

def calc2(user_input):
    tokens = user_input.split()
    
    if tokens[0] == "+":
        result = add(tokens[1], tokens[2])
        print result

    if tokens[0] == "-":
        result = subtract(tokens[1], tokens[2])
        print result

    if tokens[0] == "*":
        result = multiply(tokens[1], tokens[2])
        print result

calc2(user_input)
