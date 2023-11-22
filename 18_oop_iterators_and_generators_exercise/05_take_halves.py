def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        numbers = []
        for i in range(n):
            numbers.append(next(seq))

        return numbers

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
print()
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
