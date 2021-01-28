'''
The slicing operatorreturns a slice of the string using the syntax s[start : end].
The slice is a substring from index start to index end – 1.
If index (i or j) in the slice operation s[i : j] is negative,
replace the index with len(s) + index. If j > len(s), j is set to len(s).
If i >= j, the slice is empty
'''
s = "Programming"
print(s[1:4]) #index 1 is included and index 4 is excluded
print(s[-1 + len(s)]+" Same as "+s[-1])
print(s[: 6]) #from index 0 to 5
print(s[1 : -1])

#Concatenation of the string
s1 = "Python"
print(s + s1)
print(s+" "+s1)
print(s1 * 3) #Repeating the s1 three times.
print(3 * s)

#The in and not in Operators (Boolean Operations)
print('Prog' in s)
print('Pad' not in s)