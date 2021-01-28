def printGrade(score):
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("Fail")
def main():
    score = eval(input("Enter marks: "))
    print("Your Grade is: ", end=" ")
    printGrade(score)
main()
