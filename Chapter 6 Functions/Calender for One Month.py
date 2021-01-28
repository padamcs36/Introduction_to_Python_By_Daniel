monthName = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def monthTitle(year, month):
    print("        ",monthName[month], year,"      ")
    print("------------------------------------")
    print("  Sun  Mon  Tue  Wed  Thu  Fri  Sat ")
    monthBOdy(year, month)

def monthBOdy(year, month):
    startDay = eval(input("Enter start day of the month Sun-0 and Sat - 6:"))

    for i in range(0, startDay+1):
        print("   ", end=" ")

    for i in range(1, 31):
        print(format(i, "4d"),  end=" ")
        if (i + startDay) % 7 == 0:
            print()

def main():
    year = eval(input("Enter year : "))
    month = eval(input("Enter month of the year: "))
    monthTitle(year, month)
main()