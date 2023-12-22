def get_magic_triangle(n):
    triangle = []

    for row_i in range(n):
        current_row = []
        for col_i in range(row_i + 1):
            num = 0
            upper_col_left = col_i - 1
            upper_col_right = col_i

            if row_i == 0:
                num = 1
            else:
                if upper_col_left in range(row_i):
                    num += triangle[row_i - 1][upper_col_left]
                if upper_col_right in range(row_i):
                    num += triangle[row_i - 1][upper_col_right]

            current_row.append(num)

        triangle.append(current_row)

    return triangle


print(get_magic_triangle(5))
