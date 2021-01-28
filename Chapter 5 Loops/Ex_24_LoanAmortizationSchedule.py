# '''
# anualIntrestRate = (anual_interest / 100)
# monthlyIntresestRate = anualIntrestRate / 12
# monthlyPayment = amount * monthlyIntresestRate / (1 - 1 / (1 + monthlyIntresestRate) ** (year * 12))
# totalAmount = monthlyPayment * year * 12
# '''
# amount = eval(input("Loan Amount: "))
# year = eval(input("Number of Years: "))
# anualIntrestRate = eval(input("Anual Interest Rate: "))
#
# anualInterestRate = (anualIntrestRate / 100)
# monthlyIntresestRate = anualInterestRate / 12
# monthlyPayment = amount * monthlyIntresestRate / (1 - 1 / (1 + monthlyIntresestRate) ** (year * 12))
# totalAmount = monthlyPayment * year * 12
# print(monthlyIntresestRate)
# print("Monthly Payment : ", format(monthlyPayment, ".2f"))
# print("Total Payment: ", format(totalAmount, ".2f"))
#
# balance = amount
# for i in range(1, year * 12 + 1):
#     interest = monthlyIntresestRate * amount
#     principal = monthlyPayment - interest
#     balance = balance - principal
#     print(i,  "\t\t", interest, "\t\t", principal, "\t\t", balance)

# Enter loan amount
loanAmount = eval(input("Enter loan amount, for example 120000.95: "))

# Enter number of years
numOfYears = eval(input("Enter number of years as an integer, for example 5: "))

# Enter yearly interest rate
annualInterestRate = eval(input("Enter yearly interest rate, for example 8.25: "))

# Obtain monthly interest rate
monthlyInterestRate = annualInterestRate/1200

# Compute mortgage
monthlyPayment = loanAmount*monthlyInterestRate / \
    (1 - (pow(1 / (1 + monthlyInterestRate), numOfYears * 12)))

balance = loanAmount
print("Monthly Payment:", int(monthlyPayment * 100) / 100.0)
print("Total Payment:", int(monthlyPayment * 12 * numOfYears * 100) / 100.0)

# Display the header
print(format("Payment#", "<15s"), format("Interest", "<15s"), format("Principal", "<15s"), format("Balance", "<15s"))
for i in range(1, numOfYears * 12 + 1):
    interest = int(monthlyInterestRate * balance * 100) / 100.0
    principal = int((monthlyPayment - interest) * 100) / 100.0
    balance = int((balance - principal) * 100) / 100.0
    print(format(i, "<15d"), format(interest, "<15.2f"), format(principal, "<15.2f"), format(balance, "<15.2f"))
