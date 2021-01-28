def reverse(n):
    temp = abs(n)
    appendString = ""

    while temp != 0:
        remainder = temp % 10
        appendString += str(remainder)
        temp = temp // 10
    return appendString

value = eval(input("Enter number to reverse it: "))
print(f"{value} reversed is {reverse(value)}")