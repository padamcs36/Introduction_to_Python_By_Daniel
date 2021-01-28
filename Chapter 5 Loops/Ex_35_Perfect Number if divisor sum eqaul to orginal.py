# factor = []
# number = eval(input("Enter Integer: "))
# count = 2
# while count <= number:
#     # if number == sum(factor):
#     #     print(number)
#     while number % count == 0:
#         if number % count == 0:
#           factor.append(count)
#           number = number // count
#           count = count
#     count += 1
# print(number, sum(factor))
# # print(factor)

def perfect_number(n):
    sum = []
    sum1 = 0
    for x in range(1, n):
        if n % x == 0:
            sum.append(x)
            sum1 += x
        if sum1 == n:
            # print(n)
            sum1 = 0
            return n
print(perfect_number(28))