reversedNumber = ''

def reverse(number):
    lastNumber = number % 10
    remainingNumber = number // 10

    middle = remainingNumber % 10
    firstNumber = remainingNumber // 10

    reversedNumber = str(lastNumber) + str(middle) + str(firstNumber)
    print("Reverse Number is: ",reversedNumber)
    return isPalindrome(number)

def isPalindrome(number):
    if reversedNumber == str(number):
        print("Palindrome")
    else:
        print("Not Palindrome")

number = eval(input("Enter three digit to check for Palindrome: "))
print(reverse(number))