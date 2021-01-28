#General Formulla
# s= n/2{ 2a + (n - 1)d}
sum = 0
n = eval(input("Enter value of n: "))
for i in range(1, n+1):
    n = 1/i
    sum += n
print("Sum of Series: ",format(sum, ".2f"))

# SUM = 0
# # for i in range(n , 1, -1):
# while n >= 1:
#     k = 1/n
#     SUM += k
#     n -= 1
# print(SUM)