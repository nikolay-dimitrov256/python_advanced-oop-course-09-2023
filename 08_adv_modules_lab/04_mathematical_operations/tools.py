def calculate(first_num: float, second_num: int, operator: str):
    mapper = {'/': lambda a, b: a / b,
              '*': lambda a, b: a * b,
              '-': lambda a, b: a - b,
              '+': lambda a, b: a + b,
              '^': lambda a, b: a ** b}

    return mapper[operator](first_num, second_num)
