n, m = [int(num) for num in input().split()]

n_set = set()
m_set = set()

for _ in range(n):
    number = int(input())
    n_set.add(number)

for _ in range(m):
    number = int(input())
    m_set.add(number)

common_numbers = n_set & m_set

for num in common_numbers:
    print(num)
