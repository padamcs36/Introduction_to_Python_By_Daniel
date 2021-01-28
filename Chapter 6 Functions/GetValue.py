def main():
   nPrintln(5)
def nPrintln(n, message="Hello Python!"):
    for i in range(n):
        print(message)
main()

def sort(num1, num2):
    if num1 > num2:
        return num2, num1
    else: return num1, num2
n1, n2 = sort(9,2)
print(n1, n2)
