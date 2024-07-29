from functools import reduce

# reduce use for sum
my_list = [1, 2, 3, 4, 5]
result = reduce(
    lambda accumulator, el: accumulator + el, my_list, 0)  # start from zero
print(result)  # 15
