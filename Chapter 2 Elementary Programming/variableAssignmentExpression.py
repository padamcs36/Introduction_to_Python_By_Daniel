#prompt the user to enter three number separated by the commas
num1, num2, num3 = eval(input("Enter three number separated by commas: "))

average = (num1+num2+num3)/3
print(f"Average of {num1} + {num2} + {num3}  is {average}")

#swapping the number
x = 3
y = 5
x, y = y, x
print("Swapped number is :",x, y)