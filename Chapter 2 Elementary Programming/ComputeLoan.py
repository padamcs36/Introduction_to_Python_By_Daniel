annualInteresRate = eval(input("Enter annual interest rate: "))

#calculating the interest of one month annualInterestRate = 5.75/100*12
monthlyInterestRate = annualInteresRate / 1200
numberOfYears = eval(input("Enter number of years as an integer: "))

loanAmount = eval(input("Enter loan amount: "))
#calculating the monthly payment
monthlyPayment = loanAmount * monthlyInterestRate/(1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalAmount = monthlyPayment * numberOfYears * 12

#display results
print("The monthly payment is: ", int(monthlyPayment * 100)/100)
print("The total payment is: ", int(totalAmount * 100)/100)