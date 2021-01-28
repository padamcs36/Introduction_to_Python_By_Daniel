#Enter three digit to check wether the entered number is  palindrome or not

digit = eval(input("Enter a three-digit integer: "))

lastNumber = digit % 10
remianing = digit // 10

middleNumber = remianing % 10
firstNumber  = remianing // 10

if firstNumber == lastNumber:
    print(digit,"is a plindrome.")
else:
    print(digit,"is not a palindrome.")