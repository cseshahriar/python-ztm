n = int(input("Enter N "))
numbers = list(range(1, n))
for i, item in enumerate(numbers):
    print(f"index {i} value {item}")

print()
for i, item in enumerate(numbers, 1):
    print(list(range(0, item+1)))

print()
for i, char in enumerate("hellooooooooooooooooo"):
    print(i, char)
