def print_row(n: int, row: int):
    print(' ' * (n - row), end='')
    print(*['*'] * row)


def render_top(n: int):
    for row in range(1, n + 1):
        print_row(n, row)


def render_bottom(n: int):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def render_rhombus(n: int):
    render_top(n)

    render_bottom(n)


number = int(input())

render_rhombus(number)
