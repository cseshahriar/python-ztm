class User():
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 100)
wizard.attack()
archer.attack()

print(isinstance(wizard, User))
print(isinstance(wizard, Wizard))
print(type(wizard))
