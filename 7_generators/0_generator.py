# generator, iterablel, iterate
# In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
# Iterators are methods that iterate collections like lists, tuples, etc. Using an iterator method, we can loop through an object and return its elements.

def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


my_list = make_list(10)
# print(my_list)


"""
The yield statement suspends a function’s execution and sends a value back 
to the caller, but retains enough state to enable the function to 
resume where it left off. When the function resumes, it continues 
execution immediately after the last yield run. This allows its 
code to produce a series of values over time, rather than computing 
them at once and sending them back like a list.

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
"""


# link list
def generator_func(num):
    for i in range(num):
        yield i * 2  # yield paus the function and return value back to caller


g = generator_func(10)
print(next(g))


# iterable : __iter__
# generator actualy iterrable
