# text = list(input())
#
# while text:
#     print(text.pop(), end='')

text = list(input())
reversed_text = []

while text:
    reversed_text.append(text.pop())

print(''.join(reversed_text))
