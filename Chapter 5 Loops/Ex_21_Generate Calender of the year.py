'''
for i in range(12):
    if monthName[i] == monthName[i]:
        print(format(monthName[i],">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1,32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    print()
'''
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July", "Aug", "Sup", "Oct", "Nov", "Dec"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = eval(input("Enter Year: "))
firstDayOfTheYear = eval(input("Enter first day of the year: "))

for i in range(0, 11 + 1):
    if i == 1:
        if (months[1] % 4 == 0 and months[1] % 100 != 0) or months % 400 == 0:
            months[i] = 29
    # print(monthName[i]," 1, ", year, "is",days[firstDayOfTheYear])
    firstDayOfTheYear = (months[i] + firstDayOfTheYear) % 7
'''
if firstDayOfTheYear = 0 print(1) below sunday and continue series 
if firstDayOfTheYear = 1 print(1) below monday and continue series
if firstDayOfTheYear = 2 print(1) below Tuesday and continue series
and so on...
'''
count = 0
DIGIT_PER_LINE = 6
for i in range(12):
    if monthName[i] == "Jan":
        print(format(monthName[i],">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1,32):
            count += 1
            print(format(),format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Feb":
        print(format(monthName[i],">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1,29):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Mar":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Apr":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 31):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "May":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Jun":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 31):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "July":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Aug":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Sep":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 31):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Oct":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Nov":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 31):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    count = 0
    if monthName[i] == "Dec":
        print(format(monthName[i], ">20s"), year)
        for j in range(7):
            print(format(days[j], "<5s"), end=' ')
        print()
        for k in range(1, 32):
            count += 1
            print(format(k, "<5d"), end=' ')
            if DIGIT_PER_LINE // count == 0:
                print()
                count = 0
    print()

# import calendar
# yy = 2020
# mm = 2
# # display the calendar
# print(calendar.month(yy, mm))
# print(calendar.calendar(yy))