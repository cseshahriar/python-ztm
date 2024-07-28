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

    def run(self):
        print('ran really fast')


# multiple inheritance
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


wizard = Wizard('Merlin', 50)
archer = Archer('Robin', 100)
wizard.attack()
archer.attack()

print(isinstance(wizard, User))
print(isinstance(wizard, Wizard))
print(type(wizard))


hb1  = HybridBorg('borgin', 50, 100)
print(hb1.run())
print(hb1.attack())
