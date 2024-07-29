# filter for searching
my_list = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, my_list))
print(result)  # odd numbers [1, 3, 5]
