# == check for equality in value comparison
print(True == 1)  # true
print('' == 1)  # false
print([] == 1)  # false
print(10 == 1)  # false
print(10 == 10.0)  # true
print([] == [])  # true

print()
# is check for equality objet comparison
# is check location in memory
print(True is 1)  # false
print(True is True)  # True
print('' is 1)  # false
print([] is 1)  # false
print(10 is 1)  # false
print(10 is 10.0)  # false
print([] is [])  # false
print(1 is 1)  # True
print('1' is '1')  # True
print([1, 2, 3] is [1, 2, 3])  # False

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False
