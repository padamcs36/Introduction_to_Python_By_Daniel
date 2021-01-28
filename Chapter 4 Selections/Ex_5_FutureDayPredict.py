'''
0 - sunday, 1 - monday,  2- tuesday and sturday - 6
Now calculate the future day from the today.
'''

DayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
today = eval(input("Enter today's day (0-Sunday and 6-saturday): "))
elapsedDay = eval(input("Enter the number of days elapsed since today: "))

futureDay = (today + elapsedDay) % 7
print(f"Today is {DayList[today]} and the future day is {DayList[futureDay]}")