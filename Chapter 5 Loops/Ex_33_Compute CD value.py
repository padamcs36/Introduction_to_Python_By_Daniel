#compute CD value
#You need to import deposit amount and interest and number of months.

depositAmount = eval(input("Enter initial deposit amount: "))
interestAnual = eval(input("Enter annual percentage yield: "))
numberOfMonth = eval(input("Enter maturity period (number of months): "))

print(format("Month", "<10s"), format("CD Value"))
amount = 0
for i in range(numberOfMonth):
    OneMonthAmount = depositAmount + depositAmount * interestAnual / 1200
    # amount = OneMonthAmount + OneMonthAmount * interestAnual / 1200
    print(format(i+1, "<10d"),format(OneMonthAmount, "<.2f"))
    depositAmount = OneMonthAmount