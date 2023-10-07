text = []

try:
    with open('text.txt', 'r') as file:
        text = file.readlines()

except FileNotFoundError:
    print('File not found!')

for index, line in enumerate(text):
    if index % 2 != 0:
        continue

    line = line.strip()

    for symbol in ["-", ",", ".", "!", "?"]:
        line = line.replace(symbol, '@')

    line = list(reversed(line.split()))
    print(' '.join(line))
