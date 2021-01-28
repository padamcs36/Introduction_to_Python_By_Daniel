s = "Python"
for ch in s:
    print(s)

for i in range(0, len(s), 2):
    print(s[i], end=' ')

s = "345t"
s1 = "The3"
s2 = "343"
print("\ns.isalnum(): ", s.isalnum())
print("s1.isalpha(): ", s1.isalpha())
print("s2.isdigit(): ", s2.isdigit())
print("Padam".upper().isupper())
print("RAI".lower().isupper())