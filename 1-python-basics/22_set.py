# https://repl.it/@aneagoie/sets
# https://www.w3schools.com/python/python_ref_set.asp
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(my_set)

my_set.add(100)
print(my_set)

my_set.pop()  # set pop at first
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))
print(1 in my_set)
print(list(my_list))

new_set = my_set.copy()
print(new_set)

# new_set.clear()
# print(new_set)


diff = my_set.difference(your_set)
print('diff ', diff)

discard = my_set.discard(5)
print(discard)
print(my_set)
print(my_set.difference_update(your_set))
print(my_set)


my_set1 = {1, 2, 3, 4, 5}
your_set1 = {4, 5, 6, 7, 8, 9, 10}
print(my_set1.intersection(your_set1))  # {4, 5}
print(my_set1.isdisjoint(your_set1))  # false
print(my_set1.issubset(your_set1))  # false
print(my_set1.issuperset(your_set1))  # false
print(my_set1.union(your_set1))
print(my_set1.intersection(your_set1))
