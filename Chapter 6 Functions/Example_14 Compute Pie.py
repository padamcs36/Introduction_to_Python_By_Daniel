import math
'''
m(i) = 4  ( (-1)^i+1 / 2*i - 1)
'''
def main():
    print(format("i", "<15s"), format("m(i)"))
    i = 1
    while i < 1000:
        print(format(i, "<15d"), format(computePie(i), "0.4f"))
        i += 100
sum = 0
def computePie(i):
    global sum
    sum += math.pow(-1, i+1) / (2 * i - 1)
    return 4 * sum
main()