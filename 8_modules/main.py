import utility
from utility import multiply, divide  # best practice
from shopping.shopping_cart import buy
from shopping.more_shopping.shopping_cart import more_buy

if __name__ == '__main__':  # means if this file is run
    print('__name__', __name__)  # print module name
    num1 = float(input('Enter the number '))
    num2 = float(input('Enter the number '))
    print(utility.multiply(num1, num2))
    print(utility.divide(num1, num2))
    print(buy(num1))
    print(more_buy(num1))
