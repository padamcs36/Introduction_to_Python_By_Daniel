import math
import random
# #TODO: calculate area of circle
# radius = eval(input("Enter radius of Circle: "))
# if radius < 0:
#     print("Operation cannot be performed.")
# else:
#     area = radius * radius * math.pi
#     print("The area for the circle of radius ", radius, " is ", format(area, ".2f"))


#TODO: Program to check whether multiple of 5 or 2

# num = eval(input("Enter any number: "))
# if num % 2 == 0:
#     print("HiEven")
# if num % 5 == 0:
#     print("HiFive")

#TODO: SubtractionQuiz

# num1 = random.randint(0, 9)
# num2 = random.randint(0, 9)
#
# if num1 < num2:
#     num1, num2 = num2, num1
#
# ans = eval(input("What is "+str(num1)+" - "+str(num2)+" ?"))
#
# if num1 - num2 == ans:
#     print("You are correct")
# else:
#     print("You are wrong.\n", num1, "-", num2, "is", num1-num2)

#Todo: increase pay by 3% if score is greater than 90

# score = eval(input("Enter score: "))
# pay = eval(input("Enter your pay: "))
#
# if score >= 90:
#     per = pay * (3/100)
#     print("Your Payment is(3%): ", pay+per)
# else:
#     per = pay * (1/100)
#     print("Your Payment is(1%): ", pay+per)

#Todo: Compute BMI

# weight = eval(input("Enter wieght in pounds: "))
# height = eval(input("Enter height in inches: "))
#
# KILOGRAM_PER_POUNDS = 0.4536
# METERS_PER_INCHES = 0.0254
#
# weightInKilogram = KILOGRAM_PER_POUNDS * weight
# heightInMeters = METERS_PER_INCHES * height
# interpretation = ""
# bmi = weightInKilogram / (heightInMeters * heightInMeters)
#
# if bmi < 18.5:
#     interpretation = "Underweight"
# elif bmi >= 18.5 and bmi <=24.9:
#     interpretation = "Normal"
# elif bmi >= 25 and bmi <= 29.9:
#     interpretation = "Overweight"
# else:
#     interpretation = "Obese"
# print("BMI is",bmi)
# print(interpretation)

#Todo: ComputeTax
# status = eval(input("0-single filer, 1-married jointly, "
#                     "2-married separately, 3-head of household\n Enter filing status: "))
# income = eval(input("Enter the taxabale income: "))
# tax = 0
#
# if status == 0:
#     if income <= 8350:
#         tax = 8350 * 0.1
#     elif income > 8350 and income <= 33950:
#         tax = 8350 * 0.1 + (income - 8350) * 0.15
#     elif income > 33950 and income <= 82250:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
#     elif income > 82250 and income <= 171550:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + \
#               (income - 82250) * 0.28
#     elif income > 171550 and income <= 372950:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + \
#               (171550 - 82250) * 0.28 + (income - 171550) * 0.33
#     else:
#         tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + \
#               (171550 - 82250) * 0.28 + (372950 - 171550) * 0.33 + (income - 373950) * 0.35
# print("Tax is", format(tax, ".2f"))

#Todo: Check Errors in the Code

# income = 19000
# tax = 0
# if income <= 10000:
#     tax = income * 0.1
# elif income > 10000 and  income <= 20000:
#     tax = 10000 * 0.1 + (income - 10000) * 0.15
# print(tax)

#Todo: TO check Logical Operators
# num = eval(input("Enter any number: "))
#
# if num % 2 == 0 and num % 3 == 0:
#     print(num, "is divisible by 2 and 3.")
# if num % 2 == 0 or num % 3 == 0:
#     print(num, "is divisible by 2 or 3.")
# if (num % 2 == 0 or num % 3 == 0) and not(num % 2 == 0 and num % 3 == 0):
#     print(num, "is divisible by 2 or 3 but not both.")

#Todo: Boolean Expression is true if condition

# num = eval(input("Enter number b/w 1 and 100 or negative: "))
# condition = (num >= 1 and num <= 100) or num < 1
# print(condition)

#Todo: Check output:

# x, y, z = eval(input("Enter three numbers: "))
# print("(x < y and y < z) is", x < y and y < z)
# print("(x < y or y < z) is", x < y or y < z)
# print("not (x < y) is", not (x < y))
# print("(x < y < z) is", x < y < z)
# print("not(x < y < z) is", not (x < y < z))

#Todo: Check Wether year is leap year or not
#A year is a leap year if it is divisible by 4 but not by 100 or if it is divisible by 400
# year = eval(input("Enter year: "))
#
# leapyear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# print(year,"is a leap year?", leapyear)

# #Todo: Lottery and Win if your guess is correct.
# import random
# lottery = random.randint(0, 99)
# guess = eval(input("Enter your lottery guess pick(two digits): "))
# def getGuess():
#     lotteryDigit1 = lottery // 10
#     lotteryDigit2 = lottery %  10
#
#     guessDigit1 = guess // 10
#     guessDigit2 = guess % 10
#
#     if lottery == guess:
#         return "Exact match, You win $10000"
#     elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit1):
#         return "All digits match, You win $3000"
#     elif (guessDigit1 == lotteryDigit1 or
#          guessDigit1 == lotteryDigit2 or
#         guessDigit2 == lotteryDigit1 or
#         guessDigit2 == lotteryDigit2):
#         return "One digit Match, You win $1000"
#     else:
#         return "Sorry, No digit Match."


#Todo: TKINTER GUI
# import random
# lottery = random.randint(0, 99)
# # guess = eval(input("Enter your lottery guess pick(two digits): "))
# def getGuess():
#     lotteryDigit1 = lottery // 10
#     lotteryDigit2 = lottery % 10
#
#     guess = guessEntry.get()
#     guessDigit1 = int(guess) // 10
#     guessDigit2 = int(guess) % 10
#
#     if lottery == guessEntry.get():
#         return Label(frame, text="Exact match, You win $10000", relief=GROOVE, fg='red', bg='yellow',
#                      font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)
#
#     elif (guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit1):
#         return Label(frame, text="All digits match, You win $3000", relief=GROOVE, fg='White', bg='yellow',
#                      font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)
#
#     elif (guessDigit1 == lotteryDigit1 or
#          guessDigit1 == lotteryDigit2 or
#         guessDigit2 == lotteryDigit1 or
#         guessDigit2 == lotteryDigit2):
#         return Label(frame, text="One digit Match, You win $1000", relief=GROOVE, fg='blue', bg='yellow',
#                      font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)
#
#     else:
#         return Label(frame, text="Sorry, No digit Match.", relief=GROOVE, fg='red', bg='yellow',
#                      font=('time new roman', 14, 'bold')).grid(row=4, column=2, pady=25)
#
# from tkinter import *
# root = Tk()
# root.title("Lottery")
# root.geometry("400x400")
#
# frame = Frame(root, relief=RIDGE)
# frame.place(x=80,y=10, width=500, height=400)
# label = Label(frame, text='LOTTERY GAME', relief=GROOVE, fg='red', bg='yellow', font=('time new roman',14,'bold'))
# label.grid(row=0, column=2, pady=25)
#
# rollLabel = Label(frame, text='Guess Num:', font=('time new roman', 12, 'bold'), bg='crimson',fg='white')
# rollLabel.grid(row=1, column=2,pady=20,padx=55,sticky='w')
#
# guessEntry = StringVar()
# rollEntry = Entry(frame,textvariable=guessEntry ,font=('time new roman', 15, 'bold'), bd=5, relief=GROOVE)
# rollEntry.grid(row=2, column=2,pady=20, sticky='w')
#
# btnGuess = Button(frame, text='Guess', width=15, font=('time new roman', 12, 'bold'), command=getGuess)
# btnGuess.grid(row=3, column=2, pady=20, padx=38, sticky='w')
#
# root.mainloop()

#Todo: Expression in one line, check max number
# a, b = eval(input("Enter two number: "))
# max = a if a > b else b
# assignY = 1 if a > 0 else -1
# print("Maximum number is: ", max)
# print(assignY)

#Todo: Quadratic Equation
# a, b, c = eval(input("Enter a, b, c: "))
#
# r1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
# r2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
#
# if b**2 - 4*a*c > 0:
#     print("The roots are",format(r1,".2f"),"and",format(r2,".2f"))
# elif b**2 - 4*a*c == 0:
#     print("The root is",format(r1,".2f"))
# else:
#     print("Equation has no roots")

#Todo:Predict Future day since today

# daysInWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# today = eval(input("Enter Today's day: "))
# elapsedDay = eval(input("Enter Elapsed Day since today: "))
#
# futureday = (today + elapsedDay) % 7
# print("Today is",daysInWeek[today],"and the future day is" ,daysInWeek[futureday])

#Todo: Sort Three Number using if-else condition
