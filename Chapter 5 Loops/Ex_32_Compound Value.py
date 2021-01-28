#suppose you save $100 in each month with anual interest rate 5%
#monthly interest rate is 5/100*12 = 0.00417
#Now calculate amount of first six month.

oneMonthAmount = 100
amount = 0
for i in range(6):
    oneMonth = 100 * (1 + 0.00417)
    amount += oneMonth
    totalAmount = amount * (1 + 0.00417)
    print(format(totalAmount, ".3f"))