#Tax is 6% on the purchase amount
purchaseAmount = eval(input("Enter purchase amount: "))

tax = purchaseAmount * 0.06
print("Sales tax is: ", int(tax * 100) / 100.0)