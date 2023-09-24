rows, columns = [int(num) for num in input().split()]

char_value = 97

for row in range(rows):
    for col in range(columns):
        sides_value = char_value + row
        middle_value = char_value + row + col
        palindrome = chr(sides_value) + chr(middle_value) + chr(sides_value)

        print(palindrome, end=' ')

    print()
