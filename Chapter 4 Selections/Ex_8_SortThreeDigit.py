number1 = eval(input("Enter first number: "))
number2 = eval(input("Enter second number: "))
number3 = eval(input("Enter third number: "))

largest = number1
if number2 > largest:
    largest = number2
if number3 > largest:
    largest = number3

secondLargest = number1
if number2 < largest  and number2 > number3:
    secondLargest = number2
if number3 < largest and number3 > number2:
    secondLargest = number3

smallest = number1
if number2 < largest and number2 < secondLargest and number2 < number3:
    smallest = number2
if number3 < largest and number3 < secondLargest and number3 < number2:
    smallest = number3
print(smallest, secondLargest,largest)