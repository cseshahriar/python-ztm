# Higer order function HOC
"""
if it contains other functions as a parameter or returns a function as an output
 i.e, the functions that operate with another function are known as Higher order Functions.
"""


def shout(text):
    return text.upper()


def wisper(text):
    return text.lower()


def greet(func):
    greeting = func("Hi, I am created by a function  passed as an argument")
    print(greeting)


greet(shout)
greet(wisper)
