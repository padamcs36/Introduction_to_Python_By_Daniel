#211000 is the sale where you get the $30000 amount in one year.
BASE_SALARY = 5000
# n > 30000
sales = eval(input("Enter sale : "))
# while BASE_SALARY <= 30000:
if sales > 0 and sales <= 5000:
        BASE_SALARY = BASE_SALARY + sales * 0.08
elif sales > 5000 and sales <= 10000:
        BASE_SALARY = BASE_SALARY + (5000 * 0.08) + (sales - 5000) * 0.1
elif sales > 10000:
        BASE_SALARY = BASE_SALARY + (5000 * 0.08) + (10000 - 5000) * 0.1 + (sales - 10000) * 0.12
    # sales += 5000
print(sales, BASE_SALARY)