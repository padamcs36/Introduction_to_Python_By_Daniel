#Generate 3-digit number and guess the number
#exact number you won $10,000
#match all the number you won the $3000
#one match then you won $10,00
import random

lottery = random.randint(0, 999)
print(lottery)
lastLott = lottery % 10 #Last Digit
remainingLott = lottery // 10
secondLott = remainingLott % 10 #Middle Digit
firstLoot = remainingLott // 10 #First Digit

guess = eval(input("Enter your 3-digit Guess: "))

lastGuess = guess % 10 #Last digit
remainingGuess = guess // 10
secondGuess = remainingGuess % 10 #Middle Digit
firstGuess = remainingGuess // 10 #First Digit

if lottery == guess:
    print("Exact Match,You won $10,000.")
elif (firstGuess == lastLott and secondGuess == secondLott and lastGuess == firstLoot) or(secondGuess == firstLoot and secondGuess == secondLott and secondGuess == lastLott) or(lastGuess == firstLoot and lastGuess == secondLott and lastGuess == lastLott):
    print("All number Match")

letter = random.randint(65, 92)
print(chr(letter))