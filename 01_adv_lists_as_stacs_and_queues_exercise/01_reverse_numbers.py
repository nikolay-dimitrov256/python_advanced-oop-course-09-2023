# numbers_list = [int(num) for num in input().split()]
#
# while numbers_list:
#     print(numbers_list.pop(), end=' ')

numbers_list = [int(num) for num in input().split()]
numbers_reversed = []

while numbers_list:
    numbers_reversed.append(numbers_list.pop())

print(*numbers_reversed, sep=' ')
