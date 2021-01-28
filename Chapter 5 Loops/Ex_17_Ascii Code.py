# ! = 33, ~ = 126

count = 0
decimalValueForasci = 33
while decimalValueForasci <= 126:
    print(chr(decimalValueForasci)+" ", end='')
    count += 1
    if count == 10:
        print()
        count = 0
    decimalValueForasci += 1