class PlayerCharacter:
    membership = True  # class object attribute, not dynamic

    def __init__(self, name, age):
        # dander method or magic method, constructor
        self.name = name  # attributes
        self.age = age

    def run(self):  # method
        print("Run")
        return

    """
        There are three types of methods in Python:
            instance methods
            static methods
            class methods.
    """
    @classmethod
    def adding_things(cls, num1, num2):
        """ 
        Class methods are the third and final OOP method type to know. Class methods know about their class. They can't access specific instance data, but they can call other static methods.
        """
        return cls('salpin', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        """ 
        Static methods are methods that are related to a class in some way, but don't need to access any class-specific data. You don't have to use self, and you don't even need to instantiate an instance, you can simply call your method:
        """
        return num1 + num2


# object
player1 = PlayerCharacter('Shahriar', 29)
player1.run()
print(player1.name)

print(PlayerCharacter.membership)
print(player1.membership)  # ?

print('class method access with obj ', player1.adding_things(2, 3))
print('class method access with cls ', PlayerCharacter.adding_things(2, 3))

# https://www.makeuseof.com/tag/python-instance-static-class-methods/