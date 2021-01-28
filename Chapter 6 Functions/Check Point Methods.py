# #Program - 1
# def main():
#     max = 0
#     # getMax(1, 2, max) #Return method use print() statement
#     print(getMax(1, 2, max))
#     print(max)
# def getMax(a, b, max):
#     if a > b:
#         max = a
#     else:
#         max = b
#     return max #Now program return the value
# main()

#Program - 2:
# def main():
#     i = 1
#     while i <= 6:
#         print(function1(i, 2))
#         i += 1
# def function1(i, num):
#     line = ""
#     for i in range(1, i):
#         line += str(num)+" "
#         num *= 2
#     return line
# main()

# #Program - 3:
# def main():
#     times = 3
#     print("Before the call, variable times is ", times)
#     #invoke the method
#     nPrint("Welcome to CS", times)
#     print("After the call, variable times is ", times)
#     #after the method calling times remains same becuase the numbers and strings  are immutable
# def nPrint(message, n):
#     while n > 0:
#         print("n = ", n)
#         print(message)
#         n -= 1
# main()

#Program - 4:
def main():
    i = 0
    while i <= 4:
        function1(i)
        i += 1

        print("i is = ", i)
def function1(i):
    line = ""
    while i >= 1:
        if i % 3 != 0:
            line += str(i)+" "
            i -= 1
    print(line)
main()
