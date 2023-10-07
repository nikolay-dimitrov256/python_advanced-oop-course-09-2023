from string import punctuation

text = []

try:
    with open('text.txt', 'r') as file:
        text = file.readlines()
except FileNotFoundError:
    print('File not found!')

open('output.txt', 'w').close()

for index, line in enumerate(text):
    letters = 0
    punctuation_marks = 0
    number = index + 1
    line = line.strip()

    for ch in line:
        if ch.isalpha():
            letters += 1

        elif ch in punctuation:
            punctuation_marks += 1

    with open('output.txt', 'a') as file:
        output = f"Line {number}: {line} ({letters})({punctuation_marks})\n"
        file.writelines(output)
