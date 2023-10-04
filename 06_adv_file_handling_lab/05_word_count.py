import re

searched_words = []
text = ''
found_words_occurrences = {}

try:
    with open('words.txt', 'r') as file:
        data = file.read()
        searched_words = data.split()
except FileNotFoundError:
    pass

try:
    with open('input.txt', 'r') as file:
        text = file.read()
except FileNotFoundError:
    pass

for word in searched_words:
    pattern = rf'\b{word}\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    found_words_occurrences[word] = len(matches)

found_words_occurrences = sorted(found_words_occurrences.items(), key=lambda kvp: -kvp[1])

with open('output.txt', 'w') as file:
    for word, occurrences in found_words_occurrences:
        file.writelines(f'{word} - {occurrences}\n')
