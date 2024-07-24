# A parameter is the variable listed inside the parentheses in the function definition.
# definition is parameters
def add(a, b):  # docstrings
    ''' return a + b '''
    return a + b


# An argument is the value that are sent to the function when it is called.
# pass by value is arguments
result = add()
print(result)


# keyword args
def say_hello(name, emoji):  # name is default
    print(f"Name {name}, emoji {emoji}")


say_hello("sdfd", emoji='Salpin')  # keyword argument

# functions
print()
list()
max([4, 5])
min([3,4])
input()

# methods
message = "hello"
print(message.upper())  # upper is method