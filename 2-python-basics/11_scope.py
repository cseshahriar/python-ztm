# Scope - what var do i have access to?
# Local Variables
# Global Variables
# Nonlocal Variables
total = 100  # global scope


def sum_func():
    total = 200  # function scope
    return total


print(total)  # 1000

if True:
    x = 10

print('x', x)  # ? x is global


a = 1  # global scope

def confusion(b):
    # function scope or local scope
    a = 5  # declare new a
    # b part of local scope
    print('inside confusion of a id', id(a), 'b', b)
    return a


print('a ', a, id(a))
print('confusion ', confusion())

# Rules
# 1: start with local scope
# 2: Parent Local
# 3: Global
# 4: Built in python functions
# =============== Nonlocal===============
print()
# outside function


def outer():
    message = 'local'

    # nested function
    def inner():
        # declare nonlocal variable
        nonlocal message  # this message is parent message
        # nonlocal is outside of inner but not global
        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)


outer()
