""" utility file is a module """
print('utility __name__', __name__)


def multiply(num1, num2):
    """ multiply two numbers """
    return num1 * num2


def divide(num1, num2):
    """ divide two numbers """
    return num1 / num2


def max():
    """ override built function """
    return "oops"
