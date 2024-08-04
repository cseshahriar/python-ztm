from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array
# counter
my_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('counter ', Counter(my_list))  # frequency counter

sentece = "dfdsfsdfdfdfdfdf"
print('counter ', Counter(sentece))  # frequency counter


# defaultdict
my_dict = {'a': 1, 'b': 2, 'c': 3}
default_dict = defaultdict(lambda: 5, my_dict)  # 5 is default value
print('my dict', default_dict['d'])  # return default if not exists


# order dict
d = OrderedDict()  # order maintain
d['b'] = 2
d['a'] = 1
d['c'] = 3
print('d', d)


# datetime
print(datetime.time(5, 45, 2))  # create time object
print(datetime.date.today())


# array
my_array = array('i', [1, 2, 3])  # i for int
print(my_array)
