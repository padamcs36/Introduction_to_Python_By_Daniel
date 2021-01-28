#syntax of conditional expression
# expression1 if boolean-expression esle expression2

num = eval(input("Enter 0 or 1: "))
y = 1 if num > 0 else -1
print(y)

evenOdd = eval(input("Enter number to find even or odd: "))
print("Even number " if evenOdd % 2 == 0 else "Odd number")

age = eval(input("Enter age: "))
print("ticket Price = 20" if age >= 16 else "ticket Price = 10")

print(age if age % 10 == 0 else age)

#rewrite the expression condition into the if/else condition
# score = 3 * scale if x > 10 else 4 * scale

x = eval(input("Enter value of x: "))
scale = eval(input("Enter value of scale: "))
score = 0
if x > 10:
    score = 3 * scale
else:
    score = 4 * scale
print("Your score is: ", score)