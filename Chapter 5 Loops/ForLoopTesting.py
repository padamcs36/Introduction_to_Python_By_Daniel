# for var in range(4, 8):
#     print(var, end=' ')
#
# for var in range(1,10, 2): # 2 is increment value in the loop
#     print(var, end=' ')
#
# for var in range(5, 1, -2):
#     print(var, end=' ')

number = 0
sum = 0
for count in range(5):
    number = int(input("Enter any integer: "))
    sum += number
print("sum is : ", sum)
print("count is: ", count)