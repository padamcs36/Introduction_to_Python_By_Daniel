import math
#futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^numberOfMonths
#monthlyInterestRate = 9/100 for year => 0.09/12 for one month

def futureInvestmentValue( investmentAmount, monthlyInterestRate):
    for i in range(1, 31):
        futureInvestmentValue = investmentAmount * math.pow((1 + monthlyInterestRate), 12)
        NextYear = futureInvestmentValue
        investmentAmount = futureInvestmentValue
        print(format(i, "<15d"), format(NextYear, ".2f"))


amount = eval(input("Enter Investment Amount: "))
AnualInterestRate = eval(input("Annual Interest Rate: "))
monthlyInterestRate = AnualInterestRate/1200

print(format("Years", "15s"), format("Future Value"))
futureInvestmentValue(amount, monthlyInterestRate)

# for i in range(1, 31):
#     print(format(i, "<14d"), futureInvestmentValue(amount, monthlyInterestRate))