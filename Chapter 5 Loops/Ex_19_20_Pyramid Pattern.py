lines = eval(input("Enter number of lines: "))
for row in range (lines):
    for col in range(2 * lines):
        if (col >= lines - row and col <= lines + row):
            print(col, end=' ')
        else:
            print(end='  ')
    print()

print()
for row in range(6):
    for col in range(6):
        if col <= row:
            print(col+1, end=" ")
        else:
            print(end=" ")
    print()
print()
for row in range(1, 7):
    for col in range(1, 7):
        if col <= 7 - row:
            print(col*col, end=" ")
        else:
            print(end=" ")
    print()

