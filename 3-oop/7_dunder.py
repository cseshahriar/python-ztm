class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

    def __str__(self) -> str:
        return f"{self.color}"

    def __del__(self):
        print("deleted")

    def __call__(self):
        return True

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(action_figure['name'])
action_figure()
del action_figure
