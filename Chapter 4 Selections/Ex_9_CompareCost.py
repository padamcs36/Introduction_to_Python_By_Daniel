w1, price1 = eval(input("enter weight and price for package 1: "))
w2, price2 = eval(input("enter weight and price for package 2: "))

packg1 = (w1 / price1) * 100
packg2 = (w2 / price2) * 100

if packg1 < packg2:
    print("Package 1 has the better price.")
else:
    print("Package 2 has the better price.")