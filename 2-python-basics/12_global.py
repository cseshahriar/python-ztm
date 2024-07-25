total = 0


def count():
    # total += 1  # UnboundLocalError: local variable 'total' referenced before assignment
    global total  # use global total var
    total += 1
    return total


count()
count()
print(count())


# better way
print()
total2 = 0


def count2(total2):
    total2 += 1
    return total2


count2(total2)
count2(total2)
print(count2(total2))
