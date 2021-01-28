import math
def fib(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    num1 = num2 = 1 #Another way to find fibonacci series
    sum = 0
    for i in range(3, n+1):
        sum = num1 + num2
        num1, num2 = num2, sum
    return sum
    # return fib(n - 1) + fib(n - 2) Function is called itself (Short way to find fib)

for i in range(1, 10):
    print(i,"-->", fib(i))
print("Factorial of the Number:")
def fac(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * fac(n - 1)
for i in range(1, 10):
    print(i, "---->", fac(i))

print("Factorial with Built in function")
for i in range(1, 6):
    print(math.factorial(i))