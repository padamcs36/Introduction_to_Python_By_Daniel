import random
import sys

def main():

    dice = getDice()
    if dice == 7 or dice == 11:
        print("You win")
        sys.exit()
    if dice == 2 or dice == 3 or dice == 12:
        print("You loss")
        sys.exit()

    point = dice
    print("Point is ", dice)
    dice = getDice()
    while dice != 7 and dice != point:
        dice = getDice()

    if dice == 7:
        print("You loss")
    else:
        print("You win")

def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    print("You rolled ",i1," + ",i2," = ", i1+i2)
    return i1+i2

main()