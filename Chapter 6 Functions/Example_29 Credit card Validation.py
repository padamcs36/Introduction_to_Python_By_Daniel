def main():
    cardValid = eval(input("Enter Your ID card for Validation 13 - 16 : "))
    print("Sum of even Places: ",sumOfDoubleEvenNumber(cardValid),
          "\nSum of Odd Places: ", sumOfOddNumber(cardValid))
    isValid(cardValid)

def isValid(number):
    if (sumOfDoubleEvenNumber(number) + sumOfOddNumber(number)) % 10 == 0:
        print("The card number is Valid.")
    else:
        print("The card number is Invalid")

def sumOfDoubleEvenNumber(number):
    result1 = 0
    list = []
    while number != 0:
        remainder = number // 10
        remainder1 = remainder % 10
        singleDigit = remainder1 * 2

        if singleDigit >= 10:
            singleDigit = getDigit(singleDigit)
        list.append(singleDigit)
        result1 += singleDigit
        number = remainder // 10
    print("Even Number Places Digit: ",list)
    return result1

def getDigit(number):
    lastNumber = number % 10
    firstNumber = number // 10
    return lastNumber + firstNumber

def sumOfOddNumber(number):
    result1 = 0
    list = []
    while number != 0:
        remainder = number % 10
        remainder1 = number // 10
        result1 += remainder
        number = remainder1 // 10
        list.append(remainder)
    print("Odd Number Places Digit: ",list)
    return result1

main()