gcd = 1
k = 2
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# while k <= num1 and k <= num2:
while k <= num1/2 or k <= num2/2:
    if num2 % k == 0 and num1 % k == 0:
        gcd = k
    k += 1
print(f"Greatest common divisor for {num1} and {num2} is {gcd}")