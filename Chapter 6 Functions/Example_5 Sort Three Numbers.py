def displaySortedNumber(num1, num2, num3):

    largestNumber = num1
    if num2 > largestNumber:
        largestNumber = num2
    if num3 > largestNumber:
        largestNumber = num3

    secondLargest = num1
    if num2 < largestNumber and num2 > num3:
        secondLargest = num2
    if num3 < largestNumber and num3 > num2:
        secondLargest = num3

    smallestNumber = num1
    if largestNumber > num2 and secondLargest > num2 and num2 < num3:
        smallestNumber = num2
    if largestNumber > num3 and secondLargest > num3 and num3 < num2:
        smallestNumber = num3

    return smallestNumber, secondLargest, largestNumber

a, b, c = eval(input("Enter three number to sort in ascending order: "))
print(displaySortedNumber(a, b, c))