print("          Multiplication Table")
print("  |", end='')

for var in range(1, 11):
    print("  ",var , end=' ')
print()
print("-"*52)
for i in range(1, 11):
    print(i, "|", end='')
    for j in range(1, 11):
        print(format(i*j, "4d"), end=' ')
    print()
