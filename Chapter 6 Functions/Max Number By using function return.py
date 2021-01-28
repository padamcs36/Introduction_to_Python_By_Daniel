def max(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result
def main():
    i = eval(input("Enter num1: "))
    j = eval(input("Enter num2: "))
    print("the larger number is: ", max(i, j))
main() #call the funciton.