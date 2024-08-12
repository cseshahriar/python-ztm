# debugging

# linting
# ide / editor (pycharm)
# read errors

# pdb
import pdb


def calculate(a, b):
    pdb.set_trace()  # This sets a breakpoint
    result = a + b
    return result


print(calculate(5, 3))
"""
Basic Commands Here are some basic pdb commands you can use:
n (next): Execute the next line of code. This will step over function calls.
s (step): Step into the function calls. Use this to go inside the functions called on the current line.
c (continue): Continue execution until the next breakpoint is encountered.
l (list): List the source code around the current line.
b (break): Set a breakpoint. You can specify a line number or function name, e.g., b 10 or b my_function.
p (print): Print the value of an expression, e.g., p variable_name.
q (quit): Quit the debugger and stop the program.
"""
