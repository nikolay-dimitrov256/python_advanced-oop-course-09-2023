from tools import calculate

first_num, operator, second_num = input().split()

try:
    result = calculate(float(first_num), int(second_num), operator)
    print(f'{result:.2f}')
except ZeroDivisionError:
    print('Cannot divide by zero!')
