# Create a list of 99 Boolean elements with value False
isCovered = 10 * [False]
endOfInput = False

while not endOfInput:
    #Read number as a string from the console
    s = input("Enter line of number separated by spaces: ")
    items = s.split()
    list = [eval(x) for x in items]

    for number in list:
        if number == 0:
            endOfInput = True
        else:
            isCovered[number - 1] = True

allCovered = True
for i in range(10):
    if not isCovered[i]:
        allCovered = False
        break
if allCovered:
    print("Tickets covered all numbers")
else:
    print("Tickets don't covers all numbers")