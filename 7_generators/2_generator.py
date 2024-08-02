class MyGenerator():
    current = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if MyGenerator.current < self.end:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration


gen = MyGenerator(0, 10)
for i in gen:
    print(i)
