'''
The operators are actually methods defined in the str class.
Defining methods for operators is called operator overloading.
Operator overloading allows the programmer to use the built-in operators for
user-defined methods
Operator/Function       Method                 Description
+                       __add__(self, other)   Addition
*                       __mul__(self, other)   Multiplication
-                       __sub__(self, other)   Subtraction
/                       __truediv__(self, other) Division
%                       __mod__(self, other)   Remainder
<                       __lt__(self, other)    Less than
<=                      __le__(self, other)    Less than or equal to
==                      __eq__(self, other)    Equal to
!=                      __ne__(self, other)    Not equal to
>                       __gt__(self, other)    Greater than
>=                      __ge__(self, other)    Greater than or equal to
[index]                 __getitem__(self, index) Index operator
in                      __contains__(self, value) Check membership
len                     __len__(self)          The number of elements
str                     __str__(self) T         he string representation
'''
s1 = "Washington"
s2 = "California"
print("The first character in s1 is ", s1.__getitem__(0)) #return character at index 0
print("Concatenated s1 and s2 is ", s1.__add__(s2))
print("Padam".__mul__(5))
print(s1.__len__())
print(s1.__le__(s2))
print(s1.__ne__(s2))
print("Is W contains s1?", s1.__contains__('W')) # same as 'W' in s1
# With the help of these methods we can also perform simple arithmetic operations
a = 12
b = 5
print(a.__add__(b))
print(a.__mul__(b))
print(a.__truediv__(b))
print(a.__sub__(b))
print(a.__mod__(b))

print(s1, s1.__str__(), str(s1))