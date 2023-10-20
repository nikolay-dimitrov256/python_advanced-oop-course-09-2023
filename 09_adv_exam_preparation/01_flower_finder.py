from collections import deque

vowels_queue = deque(input().split())
consonants_stack = input().split()

searched_words = {"rose": [], "tulip": [], "lotus": [], "daffodil": []}
for word in searched_words:
    searched_words[word] = list(word)

word_found = ""

while vowels_queue and consonants_stack:
    vowel = vowels_queue.popleft()
    consonant = consonants_stack.pop()

    for word in searched_words.keys():
        while vowel in searched_words[word]:
            searched_words[word].remove(vowel)

        while consonant in searched_words[word]:
            searched_words[word].remove(consonant)

        if not searched_words[word]:
            word_found = word
            break

    if word_found:
        break


if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")
if vowels_queue:
    print(f"Vowels left: {' '.join(vowels_queue)}")
if consonants_stack:
    print(f"Consonants left: {' '.join(consonants_stack)}")
