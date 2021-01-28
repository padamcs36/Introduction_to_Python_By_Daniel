# Python uses one object for strings that have the same content
# All immutable objects with the same content are stored in one object.
#Because string is immutable objects
s1 = "Welcome"
s2 = "Welcome"
print(id(s1), id(s2))
print(len(s1))
print(max(s1))
print(min(s1))
# The indexes are 0 based; that is, they range from 0 to len(s)-1
print("First Letter '"+s1[0], "'Last Letter '"+s1[len(s1)-1]+"' of "+s1)
print(s1[-1]) #string can be access from last end with start index is -1


x = 10
y = 10
print(id(x), id(y))


