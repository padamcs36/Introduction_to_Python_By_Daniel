print("Example  1")
def funciton(x):
    print(x)
    x = 3.4 #x, y are local variable can only be accessible inside the function
    y = 4.5
    print(y)
x = 2 #Global variable can be accessible inside the function.
y = 3
funciton(x)
print(x, y)

print("Example 2")
def f(x, y = 1, z = 2):
    return x + y + z
print(f(1,1,1))
print(f(y=2,x=1,z=3))
print(f(1,z=3))

print("Find and fix the eror in the code")
def f1():
    a = 3.3
    b = 3.5
    print(a,b)
f1()
# print(a,b) NameError: name 'a' is not defined, a,b are local variable accessible inside the function
p = 10
if x < 0:
    q = -1
else:
    q = 1
print('q is ', q)