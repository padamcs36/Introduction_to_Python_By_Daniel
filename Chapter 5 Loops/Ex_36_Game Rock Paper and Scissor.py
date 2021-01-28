import random
#user won => scissor, computer => paper
#user won => rock, computer => scissor
#user won => paper, computer => rock
#When user and computer both are same the draw.
userWin = 0
compWin = 0
computerGuess = random.randint(0, 2)
userGuess = eval(input("Scissor(0), rock(1), paper(2): "))
while True:
    if computerGuess == 0 and   userGuess == 0:
        print("The  computer is Scissor, You are scissor too. It is a draw")
    if computerGuess == 0 and userGuess == 1:
        print("The computer is Scissor, You are rock, You won.")
        userWin += 1
    if computerGuess == 0 and userGuess == 2:
        print("The computer is Scissor, You are paper, You Loss")
        compWin += 1


    if computerGuess == 1 and userGuess == 0:
        print("The computer is rock, You are Scissor, You Loss")
        compWin += 1
    if computerGuess == 1 and userGuess == 1:
        print("The  computer is rock, You are rock too. It is a draw")
    if computerGuess == 1 and userGuess == 2:
        print("The compute is rock, You are paper. You won")
        userWin += 1

    if computerGuess == 2 and userGuess == 0:
        print("The computer is paper, You are Scissor, You Won")
        userWin += 1
    if computerGuess == 2 and userGuess == 1:
        print("The computer is paper, You are rock, You Loss")
        compWin += 1
    if computerGuess == 2 and userGuess == 2:
        print("The computer is paper, You are too. It is draw")

    if userWin >= 2 and not(compWin >= 2):
        print("Finally User win")
        break
    if compWin >= 2 and not(userWin >=2):
        print("Computer win")
        break

    computerGuess = random.randint(0, 2)
    userGuess = eval(input("Scissor(0), rock(1), paper(2): "))
