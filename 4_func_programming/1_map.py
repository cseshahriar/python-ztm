# map map(func, *iterables), return new list
# map for modifying the list
my_pets = ['alfred', 'tabitha', 'william', 'arla']
map_result = list(map(lambda x: x.upper(), my_pets))
print(map_result)
