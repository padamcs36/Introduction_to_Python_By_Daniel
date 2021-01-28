def getPentagonalNamber(n):
        return i * (3 * i - 1) / 2
count = 0
for i in range(1, 100):
    print(getPentagonalNamber(100), end=" ")
    count += 1
    if count % 10 == 0:
        print()