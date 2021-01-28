#Example - 1
def function1(n, m):
    # function2(3.4) it cannot be return utill and unless we are no using the return stt:\
    return function2(3.3)
def function2(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1
# function1(2, 3) it is return method, so use print() statement to call the method
print("Returned value is: ",function1(2, 4))

#Example - 2
#In min method there is no return statement, executing the code result is None.
def main():
    print("Smallest Number is: ",min(4, 6))
def min(a, b):
    smallest = a
    if b < smallest:
        smallest = b #use return statement.
    return smallest
main()

#Guess what is the error of the method.
# TypeError: '<' not supported between instances of 'tuple' and 'int'
# Tuple cannot support the < or > operators
def main1():
    #print(min1(min1(5, 6), (5, 6)) erroneous code because of tuple
    print("Smallestt Number is: ",min1(min1(2, 6), 5)) #after correction.
def min1(n1, n2):
    smallest = n1
    if n2 < smallest:
        smallest = n2
    return smallest # after courrection
main1()
