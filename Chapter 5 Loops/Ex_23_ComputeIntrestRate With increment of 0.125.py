'''
calculating the interest of one month annualInterestRate = 5.75/100*12
monthlyInterestRate = annualInteresRate / 1200
monthlyPayment = loanAmount * monthlyInterestRate/(1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalAmount = monthlyPayment * numberOfYears * 12
Starting loan intrest is 5% and ending is 8% and increment is 0.125
'''
anual_interest = 5.0 #means five 5%

amount = eval(input("Enter loan Amount: "))
year  = eval(input("Number of years: "))

print(format("Interest Rate", "<20s"), format("Monthly Payment", "<20s"),format("Total Payment"))

while anual_interest <= 8:
    anualIntrestRate = (anual_interest / 100)
    monthlyIntresestRate = anualIntrestRate / 12
    monthlyPayment = amount * monthlyIntresestRate / (1 - 1 / (1 + monthlyIntresestRate) ** (year * 12))
    totalAmount = monthlyPayment * year * 12

    print(format(anual_interest, "<20.3f"), format(monthlyPayment, "<20.3f"), format(totalAmount, "0.3f"))

    anual_interest += 0.125

