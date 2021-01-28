number = int(input("Enter an integer: "))

lastdigit = number % 10
remaingDigit = number // 10

secondlast = remaingDigit % 10
lastTwoDigit = remaingDigit // 10

thirLast = lastTwoDigit % 10
firstNumber = lastTwoDigit // 10
print(lastdigit, secondlast, thirLast, firstNumber)