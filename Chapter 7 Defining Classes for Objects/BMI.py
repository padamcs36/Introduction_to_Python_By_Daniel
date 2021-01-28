class BMI:
    def __init__(self, name, age, wieght,  height):
        self.__name = name
        self.__age = age
        self.__weight = wieght
        self.__height = height

    def getBMI(self):
        KILOGRAM_PER_POUND = 0.45359237
        METER_PER_INCH = 0.0254
        bmi = self.__weight *  KILOGRAM_PER_POUND / (self.__height * METER_PER_INCH) ** 2
        return round(bmi * 100 / 100)

    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underwieght"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overwieght"
        else:
            return "Obese"

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeight(self):
        return self.__height

