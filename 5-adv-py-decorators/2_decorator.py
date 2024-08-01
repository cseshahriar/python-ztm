from time import time
# decorator: A decorator is a design pattern in Python that allows a user
# to add new functionality to an existing object without modifying its
# structure.


# Decorator patttern
# add new functionality
def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Function {fn.__name__} executed in {end_time - start_time} ms")
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()