# truthy and falsy
is_old = "hello"
is_licensed = 5
# is_licensed = bool(5)
if is_old:
    print("You are old enough to drive!")
elif is_licensed:
    print("You can drive!")
else:
    print('You are not of age!')

# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
print(bool(''))
print(bool(0))
print(bool(1))
print(bool('a'))

"""
falsy values
None, 0, 0.0 0j, Decimal(0)
Fraction(0, 1)
[] empty list
{} empty dict
set() en empty set
() empty tuple
'' en empty str
b'' en empty bytes
and empty range like range(0)
objects for which
 obj.__bool__() return false
 obj.__len__() return 0

"""
# others are truthy values

# my_set = set() # empty set
my_set = {1, 2, 3}  # empty set
my_dict = {}

print(type(my_set), type(my_dict))
