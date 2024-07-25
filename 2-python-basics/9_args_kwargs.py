# *args **kwargs
def super_func(name, *args, **kwargs):  # parameter
    print('args: ', args, type(args))
    print('kwargs: ', kwargs, type(kwargs))
    return sum(args)


# argument pass
print(super_func('shahriar', 1, 2, 3, 4, 5, age='29'))

# Rules: params, *args, default parameters, ** kwargs
