import re

input_string = input()

# Valid emoji: Surrounded by ** or :: (Exactly 2), at least 3 chars long(without the surrounding chars), starts with
# a capital letter, continues with lowercase only

emoji_matcher = r'(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=surr)'
digit_matcher = r'\d'

all_digits = [int(num) for num in re.findall(digit_matcher, input_string)]

cool_threshold = 1
for num in all_digits:
    cool_threshold *= num

print(f'Cool threshold: {cool_threshold}')

cool_emojis = []
emoji_count = 0

for emoji in re.finditer(emoji_matcher, input_string):
    emoji_count += 1
    data = emoji.groupdict()
    emoji = data['emoji']
    emoji_coolness = sum([ord(letter) for letter in emoji])

    if emoji_coolness >= cool_threshold:
        cool_emojis.append(data['surr'] + emoji + data['surr'])

print(f'{emoji_count} emojis found in the text. The cool ones are:')
print('\n'.join(cool_emojis))
