# find square root of the n by using below formulla.
#suppose starting guess is 1, now 1 is the starting value of the lastguess
#if the difference between nextGuess and lastGuess is very small, we can claim that
# nextGuess is approximated sqaure root of n. if not then continue this process.
# nextGuess = (lastGuess + (n / lastGuess)) / 2

def main():
    n = eval(input("Enter n: "))
    sqrt(n)

def sqrt(n):

    Lastguess = 1
    lastGuess = eval(input("Enter your first Guess: "))
    while Lastguess != -1:

        nextGuess = (lastGuess + (n / lastGuess)) / 2
        lastGuess = nextGuess
        print(nextGuess, lastGuess)

        Lastguess = eval(input("do you want to quit then enter -1:  "))

main()