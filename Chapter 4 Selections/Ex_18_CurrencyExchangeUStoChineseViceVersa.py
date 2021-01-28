#Program to covert Chinese RMB into the US Dollar and vice Versa
#When user enter 0 then covert dollar into the  yuan
#when user enter 1 then convert RMB into  the dollar

conversion = eval(input("Enter the exchange rate from dollars to RMB: "))
checkCondition = eval(input("Enter 0 to convert dollars to RMB and 1 Vice Versa: "))

if checkCondition == 0:
    dollarAmount = eval(input("Enter dollar amount: "))
    RMB = conversion * dollarAmount
    print(f"{dollarAmount * 10 / 10.0} dollar is {RMB} yuan")

elif checkCondition == 1:
    RMBAmount = eval(input("Enter the RMB amount: "))
    dollar = RMBAmount / conversion
    print(f"{RMBAmount * 10 / 10.0} yuan is {dollar * 100 / 100.0} dollars")
else:
    print("Incorrect Input")