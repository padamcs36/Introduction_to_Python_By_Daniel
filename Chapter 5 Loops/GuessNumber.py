import random
number = random.randint(0,100)

print("Guess the magic number between 0 and 100")
count = 0
guess = -1
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Yes, the number is ", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("You guess is too low")
    count += 1
print("Loop executed : ", count)