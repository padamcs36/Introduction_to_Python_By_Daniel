import random
HeadTail = random.randint(0, 1)
# print(HeadTail)

userGuess = eval(input("Enter 1-Head, 0-Tail: "))

if userGuess == HeadTail:
    print("You won the Toss")
else:
    print("You loss the Toss.")