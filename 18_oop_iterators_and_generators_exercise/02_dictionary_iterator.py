class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict_items = tuple(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict_items):
            raise StopIteration()

        i = self.index
        self.index += 1
        return self.dict_items[i]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print()
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
