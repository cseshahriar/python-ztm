# MRO - Method resolution order
# Bottom to up rules

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


# A -> C -> D -> B -> A

print(D.num)  # 1 means c
# d -> b -> a -> num
# d -> c -> num  # so this shortest path
print(D.mro())
"""
[
    <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
    <class '__main__.A'>, <class 'object'>
]
"""
# first check d
# then check b
# then check c (found)
