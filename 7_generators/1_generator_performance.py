
# link list
def generator_func(num):
    for i in range(num):
        yield i * 2  # yield paus the function and return value back to caller


g = generator_func(10)
print(next(g))


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3, 4])
