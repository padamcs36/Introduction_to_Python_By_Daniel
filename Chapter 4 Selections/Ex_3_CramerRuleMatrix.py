'''
find the value of x and y from the given equation by using cramer method
ax + by = e, cx + dy = f
x = ed - bf / ad - bc
y = af - ec / ad - bc
'''

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

# x = (e * d - b * f) / (a * d - b * c)
# y = (a * f - e * c) / (a * d - b * c)

disc = a * d - b * c
if disc == 0:
    print("The eqaution has no solution.")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)

    print(f"x is {x} and y is {y}")