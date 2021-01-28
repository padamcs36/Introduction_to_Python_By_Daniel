import RandomCharacter

NUMBER_OF_CHARACTER = 175
CHARS_PER_LINE = 25

for i in range(NUMBER_OF_CHARACTER):
    print(RandomCharacter.getRandomLowerCaseLetter(), end='')
    if (i+1) % CHARS_PER_LINE == 0:
        print()
print()
for i in range(NUMBER_OF_CHARACTER):
    print(RandomCharacter.getRandomUperCaseLetter(), end='')
    if (i+1) % CHARS_PER_LINE == 0:
        print()