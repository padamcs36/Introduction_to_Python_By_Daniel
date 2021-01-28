number = eval(input("Enter any number: "))

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisble by 2 and 3")
if number % 2 == 0 or number % 3 == 0:
    print(number,"is divisble by 2 or 3")
if (number % 2 == 0 or number % 3 == 0) and not(number % 2 == 0 and number % 3 == 0):
    print(number,"is divisible by 2 or 3, but not both")

#De Morgan's Law
# not(a or b) = not (a  and  b)
if not(number % 2 == 0 or number % 3 == 0):
    print(number, "LHS")
else:
    print("False")
if number % 2 != 0 and number % 3 != 0:
    print(number, "RHS")
else:
    print("False")

x = 1
print(True and (3 > 4))
print((x > 0) or (x < 0))
print(int(True))