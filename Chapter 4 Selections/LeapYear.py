#Finding wether the given year is leap year or not

year = eval(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year,"is a leap year!")
else:
    print(year,"is not a leap year!")