# Dictionary
# https://www.w3schools.com/python/python_ref_dictionary.asp
# https://repl.it/@aneagoie/dictionary

dictionary = {  # key: value
    'numbers': [1, 2, 3, 4],
    'name': 'Shahriar',
    'age': 29,
    'occupation': "Full Stack Developer"
}
print(dictionary)
print(dictionary.get('name'))
print(dictionary['age'])
print(dictionary['occupation'])
print(dictionary['numbers'][0])

users = [
    {'name': 'Shahriar', 'password': 'admin123#'},
    {'name': 'Shahriar1', 'password': 'admin123#'},
    {'name': 'Shahriar2', 'password': 'admin123#'},
]

for person in users:
    print(f"name {person['name']} password {person['password']}", end='\n')


# dictionary methods
print()
users = {
    "basket": [1, 2, 3],
    "greet": "hello",
    "age": 29
}
print(users['basket'])
print(users.get('age', 30))

user2 = dict(name='Shahriar')
print(user2)

print('basket' in users)  # key check
print('basket' in users.keys())  # key check
print('hello' in users.values())  # value check

print(users.items())
print(users.keys())
print(users.values())

users2 = users.copy()
users.clear()
print(users)
print(user2)


users3 = {
    "basket": [1, 2, 3],
    "greet": "hello",
    "age": 29
}
print(users3.pop('age'))
print(users3)
