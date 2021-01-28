from random import randint
#Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))

#Generate a random Lowercase letter
def getRandomLowerCaseLetter():
    return getRandomCharacter('a', 'z')

#Generate a random Uperrcase letter
def getRandomUperCaseLetter():
    return getRandomCharacter('A', 'Z')

#generate random digit character
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')

#Generate a random character
def getRandomASCIICharacter():
    return chr(randint(0, 127))