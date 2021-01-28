YEAR_PER_LINES = 10
count = 0

for i in range(2001, 2100 + 1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        print(i, end=' ')
        count += 1
        if YEAR_PER_LINES // count == 0:
            print()
            count = 0