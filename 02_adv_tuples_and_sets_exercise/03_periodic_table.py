n = int(input())

unique_elements = set()

for _ in range(n):
    line = input().split()
    unique_elements.update(line)

print('\n'.join(unique_elements))
