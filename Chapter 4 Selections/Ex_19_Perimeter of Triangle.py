a, b, c = eval(input("Enter three edges of Triangle: "))

if a + b > c and a + c > b and b + c > a:
    perimter = a + b + c
    print("The perimmeter is ", perimter)
else:
    print("The input is Invalid")