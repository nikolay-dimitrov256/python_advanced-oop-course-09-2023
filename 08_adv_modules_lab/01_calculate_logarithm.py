from math import log

number = int(input())
base = input()

try:
    base = int(base)
    result = log(number, base)
except ValueError:
    result = log(number)

print(f'{result:.2f}')
