'''
Employee’s name (e.g., Smith)
Number of hours worked in a week (e.g., 10)
Hourly pay rate (e.g., 9.75)
Federal tax withholding rate (e.g., 20%= 0.20)
State tax withholding rate (e.g., 9%=0.09)
'''
name = input("Enter Employee name: ")
noOfHourWorked = eval(input("Enter number of hours worked in a week: "))
HourlyPayRate = eval(input("Enter hourly pay rate: "))
federalTax = eval(input("Enter federal tax withholding rate: "))
stateTax = eval(input("Enter state tax withholding rate: "))

grosspay = noOfHourWorked * HourlyPayRate
cutfederalTax = grosspay * federalTax
cutStateTax = grosspay * stateTax
totalDeduction = cutfederalTax + cutStateTax
netPay = grosspay - totalDeduction

print("\n\nEmployee Name: ", name)
print("Hours Worked: ", noOfHourWorked)
print("Pay Rate: $",HourlyPayRate)
print("Gross Pay: $",grosspay)
print("Deductions: ")
print("    Federal Withholding (20.0%): $",cutfederalTax)
print("    State Withholding (9.0%): $",cutStateTax)
print("    Total Deduction: $",totalDeduction)
print("Net Pay: $",netPay)