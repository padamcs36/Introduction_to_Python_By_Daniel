#if the discriminat is greater than zero = two roots
#if discriminant == 0 one root
#if discriminant < 0 no real root

a, b, c = eval(input("Enter a, b, c: "))

r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a

disc = b ** 2 - 4 * a * c

if disc > 0:
    print(f"The roots are {r1} and {r2}")
elif disc == 0:
    print(f"The root is {r1}")
else:
    print("The equation has no real roots.")