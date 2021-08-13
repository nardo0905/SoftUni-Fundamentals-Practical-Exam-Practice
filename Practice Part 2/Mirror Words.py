import re

text = input()

matcher = r"(@|#)(?P<word_one>[a-zA-Z]{3,})(\1)(\1)(?P<word_two>[a-zA-Z]{3,})(\1)"

valid_pairs = re.finditer(matcher, text)

valid_pairs_count = 0
mirror_count = 0
mirrored_words = []

for match in valid_pairs:

    valid_pairs_count += 1
    first_word = match.group('word_one')
    second_word = match.group('word_two')
    second_word_reversed = second_word[::-1]

    if first_word == second_word_reversed:
        mirror_count += 1
        mirrored_words.append(f"{first_word} <=> {second_word}")

if valid_pairs_count > 0:
    print(f'{valid_pairs_count} word pairs found!')
else:
    print('No word pairs found!')

if mirror_count <= 0:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(mirrored_words))
