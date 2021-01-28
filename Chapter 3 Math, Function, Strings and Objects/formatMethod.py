amount = 14949.4
interestRate = 0.00422
interest = amount * interestRate
print("Interest is ", interest)
print("Interest is ", format(interest, ".2f")) #by default width is 0

print(format(5859.543, "10.2f")) # 10 is width, 2 is precision after decimal point, f dtype
print(format(43.5, "10.2f"))

print(format(949933.003, ".5e"))
print(format(57, "10.2e"))

print(format(48, ".2%")) #it is multiplying with 100 and display the result with %

#Justifying Format
#By default number is right justify
#If you want number is display from left then put (<)=>left Justified
print(format(33.44, "10.2f"))
print(format(33.44, "<10.2f"))
print(format(33.44, ">10.2f"))
print(format(33.44, "^10.2f")) # display with equal on both side

for i in range(1,10,2):
    print('{^:12}'.format('*'*i))

for i in range(1, 10, 2):
    print('{:>15}'.format('*'*i))
    #: means print  all star in first iteratin 1, 3, 5, 7, 9
    # >15 is right justified with 15 space