for _ in range(10):
    print("Hello", end=" ")

print()
for i in range(0, 10, 1):
    print(i, end=" ")


print()
for i in range(0, 10, 2):
    print(i, end=" ")

print()
for i in range(1, 10, 2):
    print(i, end=" ")

print()
for i in range(10, 0, -1):  # revere
    print(i, end=" ")


print()
my_list = list(range(1, 11))
for i in my_list:  # sub array
    print(list(range(i)))

print()
for i in range(len(my_list) + 1):  # sub array
    print(my_list[0:i])
