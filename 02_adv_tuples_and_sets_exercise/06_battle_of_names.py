n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    name_value = sum([ord(ch) for ch in name]) // row
    if name_value % 2 != 0:
        odd_set.add(name_value)
    else:
        even_set.add(name_value)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(*odd_set | even_set, sep=', ')
elif odd_sum > even_sum:
    print(*odd_set - even_set, sep=', ')
elif even_sum > odd_sum:
    print(*odd_set ^ even_set, sep=', ')
