import random
#user won => scissor, computer => paper
#user won => rock, computer => scissor
#user won => paper, computer => rock
#When user and computer both are same the draw.
computerGuess = random.randint(0, 2)
userGuess = eval(input("Scissor(0), rock(1), paper(2): "))

if computerGuess == 0 and userGuess == 0:
    print("The  computer is Scissor, You are scissor too. It is a draw")
elif computerGuess == 0 and userGuess == 1:
    print("The computer is Scissor, You are rock, You won.")
elif computerGuess == 0 and userGuess == 2:
    print("The computer is Scissor, You are paper, You Loss")


elif computerGuess == 1 and userGuess == 0:
    print("The computer is rock, You are Scissor, You Loss")
elif computerGuess == 1 and userGuess == 1:
    print("The  computer is rock, You are rock too. It is a draw")
elif computerGuess == 1 and userGuess == 2:
    print("The compute is rock, You are paper. You won")

elif computerGuess == 2 and userGuess == 0:
    print("The computer is paper, You are Scissor, You Won")
elif computerGuess == 2 and userGuess == 1:
    print("The computer is paper, You are rock, You Loss")
elif computerGuess == 2 and userGuess == 2:
    print("The computer is paper, You are too. It is draw")