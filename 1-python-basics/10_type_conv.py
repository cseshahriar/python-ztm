# https://realpython.com/python-comments-guide/
print(str(100))
print('Hello' + str(100))
print(5 + int('100'))

birth_day = input("what year were you born? ")
print(birth_day)
age = 2019 - float(birth_day)
age = 2019 - bool(birth_day)  # true value is 1
print(f'your age is: {age}')
