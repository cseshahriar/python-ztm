# list, also data structure, mutable
# https://www.w3schools.com/python/python_ref_list.asp
# https://repl.it/@aneagoie/lists-2

numbers = [1, 2, 3, 4, 5]
latters = ['a', 'b', 'c']
alpha_numeric = [1, 'a', True]

numbers[0] = 1000
for i in numbers:
    print(i, end=" ")

print('\n')
# https://repl.it/@aneagoie/lists

# LIST SLICING
print(numbers[0:2])
print(numbers[0:5:1])  # start, stop, step over
print(numbers[0:5:2])  # print odd
print(numbers[0::2])
print(numbers[::-1])  # reverse
print(numbers[0])

new_numbers = numbers[0::2]
another_new_numbers = numbers[:]  # copy
print(new_numbers)
print(another_new_numbers)


print("List methods ")
# list methods
print(len(numbers))

# adding
numbers.append(100)
print('append item 100 ', numbers)

# append multiple elements
numbers.extend([11, 22, 33])
print(numbers)

# insert
numbers.insert(0, 5000)
print(numbers)

# remove
numbers.pop()
print('pop last', numbers)

numbers.pop(1)
print('pop at index 1 ', numbers)

numbers.remove(5000)
print('remove value 5000', numbers)

numbers.clear()
print('clear ', numbers)

numbers.extend([1, 2, 3, 4, 5])
print(numbers.index(2))  # value, start, stop

basket = ['x', 'a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d', 0, 6))  # 0 to 2 search
print('x' in basket)
print(basket.count('d'))

# https://www.w3schools.com/python/python_ref_keywords.asp
basket.sort()
print(basket)

# basket.sort(reverse=True)
# print(basket)

# basket.reverse()
# print(basket)

# new_basket = basket[:]
new_basket = basket.copy()
new_basket.sort()
print(new_basket)  # produced new list, not modify


# common list pattern
print(basket[::-1])  # reverse, create new list
print(basket)

# my_list = list(range(1, 100))
my_list = list(range(101))
print(my_list)

sentence = ''
new_sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Shahriar'])
print(new_sentence)

# https://repl.it/@aneagoie/lists-3

# list unpacking
basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, c, *d = basket
print(a)
print(b)
print(c)
print(d)
