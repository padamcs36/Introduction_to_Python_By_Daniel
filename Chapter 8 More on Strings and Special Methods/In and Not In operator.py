s = input("Enter a string :=>")
if 'Python' in s:
    print("Python"," is in", s)
else:
    print("Python","is not in ",s)

s1 = input("enter first string: ")
s2 = input("enter second string: ")

if s1 < s2:
    s1, s2 = s2, s1
print("the two strings are in this order ",s1, s2)