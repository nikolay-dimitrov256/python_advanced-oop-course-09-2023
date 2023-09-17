expression = input()
indexes = []

for i in range(len(expression)):

    if expression[i] == '(':
        indexes.append(i)

    elif expression[i] == ')':
        first_index = indexes.pop()
        last_index = i + 1

        print(expression[first_index:last_index])
