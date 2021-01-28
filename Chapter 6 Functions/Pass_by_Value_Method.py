# def main():
#     max = 0
#     # getMax(1, 2, max) return type you must use print() function to get value
#     print(getMax(1, 2, max))
#     print(max)
# def getMax(a, b, max):
#     if a > b:
#         max = a
#     else:
#         max = b
#     return max
# main()

#Example - 2
def main():
    i = 1
    while i <= 6:
        print(function1(i, 2))
        i += 1
def function1(i, num):
    line = ""
    for j in range(1, i):
        line += str(num)+" "
        num *= 2
    return  line
main()


def gcd(n1, n2):
    gcd = 1
    k = 2
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return  gcd