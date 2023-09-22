size = int(input())

matrix = [list(input()) for _ in range(size)]
searched_symbol = input()

for row_i in range(size):
    for col_i in range(size):

        if matrix[row_i][col_i] == searched_symbol:
            print((row_i, col_i))
            exit()

print(f'{searched_symbol} does not occur in the matrix')
