class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    num = int(input())

    if num < 0:
        raise ValueCannotBeNegative('Entered an integer below 0! Please enter a positive integer!')
