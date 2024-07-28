class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 60, 'merling@gmail.com')
print(wizard1.email)

# introspection
print(dir(wizard1))
