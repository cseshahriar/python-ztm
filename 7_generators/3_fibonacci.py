from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Function {fn.__name__} executed in {end_time - start_time} ms")
        return result
    return wrapper


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
# f(n-2) = fn - f (n-1)

@performance
def fib(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)  # add to list at the end
        temp = a
        a = b  # first el
        b = temp + b  # second el
    return result


@performance
def fib_generator(n):  # generator work one by one
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b  # first el
        b = temp + b  # second el


fib(100000)  # 0.181 ms
fib_generator(100000)  # 143 ms

"""
Function fib executed in 0.1817770004272461 ms
Function fib_generator executed in 1.430511474609375e-06 ms
"""
