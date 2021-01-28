import random

lottery = random.randint(0, 99)
guess = eval(input("Enter your lottery (pick two number): "))

lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

guessNum1 = guess // 10
guessNum2 = guess % 10

print("Lotter number are : ",lottery)
if guess == lottery:
    print("Exact Match! You won $10,000")
elif guessNum1 == lotteryDigit2 and guessNum2 == lotteryDigit1:
    print("Match all digit! you won $3,000")
elif (guessNum1 == lotteryDigit1 or
      guessNum1 == lotteryDigit2 or
      guessNum2 == lotteryDigit1 or
      guessNum2 == lotteryDigit2):
    print("Match one digit! you won $1,000")
else:
    print("Sorry, no match!")