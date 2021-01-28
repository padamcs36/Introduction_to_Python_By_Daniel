sum = 0
def sumDigits(n):
    lastDigit = n % 10
    remainingDigit = n // 10

    middlleDigit = remainingDigit % 10
    firstDigit = remainingDigit // 10

    sum = lastDigit + middlleDigit + firstDigit
    return sum
enterDigit = eval(input("Enter digits to find out their sum: "))
print("Sum of Digits is: ", sumDigits(enterDigit))