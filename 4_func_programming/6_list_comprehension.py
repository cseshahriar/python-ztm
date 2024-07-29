# list, set, dict comprehension
my_list = list(range(10))
result = [
    x * 2
    for x in my_list
    if x % 2 != 0
]
print(result)

letters = [ch for ch in 'abcd']
print(letters)

# set
letters = {ch for ch in 'abcd'}
print(letters)


# set
letters = [{"letter": ch} for ch in 'abcd']
print(letters)
