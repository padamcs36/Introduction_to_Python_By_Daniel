positive = 0
negative = 0
total = 0
sum = 0
integerNum = eval(input("Enter an integer, the input ends if it is 0: "))
if integerNum != 0:
    while integerNum != 0:
        if integerNum > 0:
            positive += 1
        if integerNum < 0:
            negative += 1
        sum += integerNum
        total += 1
        integerNum = eval(input("Enter an integer, the input ends if it is 0: "))

    print("The number of positive is ", positive)
    print("The number of negative is ", negative)
    print("The total is ", total)
    print("The average is ", sum / total)
else:
    print("You did'nt enter any number")
