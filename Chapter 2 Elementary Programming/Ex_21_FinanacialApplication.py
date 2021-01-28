'''
Suppose you save $100 each month into a saving acount with an annual
ineterest rate of 5%. find amount after sixth month
month interest rate = 5/100*12 = 0.00417
'''

monthlySaving = eval(input("Enter the monthly saving amount: "))

firstMonth = 100 * (1 + 0.00417)
secondMonth = (100 + firstMonth ) * (1 + 0.00417)
thirdMonth = (100 + secondMonth ) * (1 + 0.00417)
fourthMonth = (100 + thirdMonth ) * (1 + 0.00417)
fifthMonth = (100 + fourthMonth ) * (1 + 0.00417)
sixthMonth = (100 + fifthMonth ) * (1 + 0.00417)
print("After the sixth month, the acount value is ", int(sixthMonth * 100)/100.0)