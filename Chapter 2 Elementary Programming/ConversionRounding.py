#when one value in integer and other in float the python interpreter it into the
#float itself without any coversion

print(4 * 3.5)
var = 5.5
print(int(var)) #result is 5

print(round(var)) #result is 6
print(eval("3 + 4")) # this more efficient method to covert expression into the number
print(eval("3.4"))
#print(int("3 + 4")) this is not work in this expression

print(int("0003")) #In this case this more favoureable than eval() function
# print(eval("003")) cause syntaxError