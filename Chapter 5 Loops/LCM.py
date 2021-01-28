n1, n2 = eval(input("Enter two an integer >= 2: "))
factor = 2
lcm = 1
while factor <= n1 and factor <= n2:
    if n1 % factor == 0 and n2 % factor == 0:
        break
    else:
        print("No factor other than one.")
    factor += 1

print(f"The smallest factor other than 1 of {n1} and {n2} is {factor}")
if n1 > n2:
    greater = n1
else:
    greater = n2
while(True):
    if((greater % n1 == 0) and (greater % n2 == 0)):
        lcm = greater
        break
    greater += 1
print(f"LCM of {n1} and {n2} is {lcm}")
