# tuple
# https://www.w3schools.com/python/python_ref_tuple.asp
my_tuple = (1, 2, 3, 4, 5, 5)  # immutable: cant change vale, can add, remove
print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

print(my_tuple[::2])  # step 2
print(my_tuple[::-1])  # reverse
new_tuple = my_tuple[1:3]
print(new_tuple)
print(len(my_tuple))

x, y, z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)
print('count of 5', my_tuple.count(5))  # 2 times
print('index of 5', my_tuple.index(5))
print('len', len(my_tuple))
