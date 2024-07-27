"""
Encapsulation is a fundamental object-oriented principle in Python.
It protects your classes from accidental changes or
deletions and promotes code reusability and maintainability.

In other OOP languages such as Java and C++, encapsulation is strictly enforced
with access modifiers such as public, private or protected, but Python doesn't have those.
"""


class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  # protected member
        self.__age = age  # private member

    def run(self):  # method
        print("Run")
        return

    def speak(self):
        print(f"My name is {self._name}, and I am {self.__age} years old.")

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


# object
player1 = PlayerCharacter('Shahriar', 29)
player1.speak()
print(player1._name)  # protected can

# print(player1.__age)  # ca't access private outside of class
# access by own class public method
player1.set_age(33)
print(player1.get_age())
