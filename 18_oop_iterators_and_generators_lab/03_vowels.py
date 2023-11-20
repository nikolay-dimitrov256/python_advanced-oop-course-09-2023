class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = [ch for ch in self.text if ch.lower() in 'aeiuyo']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.vowels):
            raise StopIteration()
        i = self.index
        self.index += 1
        return self.vowels[i]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
