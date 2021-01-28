#Combination of two digits
i = 1
count = 0
combinationCount = 0
enterNoOfCombination = eval(input("Enter number of combination: "))
while i <= enterNoOfCombination:
    j = 2
    while j <= enterNoOfCombination:
        if (j+count) > enterNoOfCombination:
            break
        print(f"{i, j+count}", end=' ')
        combinationCount += 1
        j += 1
    count += 1
    print()
    i += 1
print("Total Number of Combination of Two Numbers is: ",combinationCount)