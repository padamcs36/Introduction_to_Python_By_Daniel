from BMI import BMI
def main():
    bmi1 = BMI("John", 18, 145, 70)
    print("BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())

    bmi2 = BMI("Padam", 23, 91, 70)
    print("BMI for ", bmi2.getName(), "is", bmi2.getBMI(), bmi2.getStatus())

main()