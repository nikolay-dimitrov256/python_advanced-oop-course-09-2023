class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration()

        self.iterations += 1
        current = self.current
        self.current += self.step
        return current


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print()
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
