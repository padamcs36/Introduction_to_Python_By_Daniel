def main():
    print(format("i", "<15s"), format("m(i)"))
    i = 1
    while i <= 20:
        print(format(i, "<15d"), format(sumSeries(i), "0.4f"))
        i += 1
sum = 0
def sumSeries(i):
    global sum
    m = i / (i + 1)
    sum += m
    return sum
main()