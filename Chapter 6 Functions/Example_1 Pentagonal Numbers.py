#Pentagonal number is defined as n(3n - 1)/2
#Total Pentagonal Numbers = 100
#Per line is 10
Per_line = 10
def getPentagonalNumber(n):
        pentagonalNumber = int(n * (3 * n - 1) / 2)
        print(pentagonalNumber, end=' ')

numbers = eval(input("Enter pentagonal number do you want: "))
for i in range(numbers):
    getPentagonalNumber(i+1)
    if (i+1) % Per_line == 0:
        print()