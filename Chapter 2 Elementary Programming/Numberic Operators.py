#+, -, x, /, //, **, %
# Precedence of the operators
'''
1.Brackest ()
2. ** exponential
3. *,/,//,%
4. *,/,//,% multiple in the expression then solved from left to right
5. +, - => solved from  left to right

'''
print(3," + ", 4, " = ", 3 + 4)
print(3," - ", 4, " = ", 3 - 4)
print(3," * ", 4, " = ", 3 * 4)
print(3," / ", 4, " = ", 3 / 4) #float division
print(3," // ", 4, " = ", 3 // 4) #Integer division
print(5," ** ", 4, " = ", 5 ** 4) #Exponential Power
print(5," % ", 4, " = ", 5 % 4) #Modulus=it returns the remainder of the division

print("45 + 4 * 4 - 2 = ", 45 + 4 * 4 - 2)
print("45 + 43 % 5 * (23 * 3 % 3) = ", (45 + 43 % 5 * (23 * 3 % 3)))  #3 % 3=0 answer = 45
print(23 * 3 % 3) #percedence of % is higher than *