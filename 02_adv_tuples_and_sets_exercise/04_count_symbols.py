text = tuple(input())

unique_characters = set(text)

for ch in sorted(unique_characters):
    print(f'{ch}: {text.count(ch)} time/s')
