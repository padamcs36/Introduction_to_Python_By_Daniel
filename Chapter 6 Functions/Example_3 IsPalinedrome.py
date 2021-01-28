def Reverse(number):
    temp = abs(number)
    appendNumber = ""

    while temp != 0:
        remainder = temp % 10
        appendNumber += str(remainder)
        temp = temp // 10
    return appendNumber

def isPalindrome(number):
    reversedNumber = Reverse(number)

    if number == int(reversedNumber):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

value = eval(input("Enter number to check wether Palindrome or not: "))
isPalindrome(value)