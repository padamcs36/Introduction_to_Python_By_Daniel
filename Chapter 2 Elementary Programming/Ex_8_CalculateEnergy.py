water = eval(input("Enter amount of water in kilograms: "))
temp1 = eval(input("Enter initial temperature: "))
temp2 = eval(input("Enter final temperature: "))

energy = water * (temp2 - temp1) * 4184
print(" The Energy needed is ", energy)