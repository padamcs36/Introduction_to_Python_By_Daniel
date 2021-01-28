#print number of days in year from 2010 to 2020.
def main():
    print(format("Year","<10s"),format("Days"))
    i = 2010
    while i <= 2020:
        print(format(i,"<10d"),format(numberOfDayinYear(i)))
        i += 1

def numberOfDayinYear(year):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 366
    else:
        return 365
main()