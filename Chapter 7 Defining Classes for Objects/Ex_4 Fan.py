class Fan:
    def __init__(self, speed = 1, on = False, radius = 5, color = "BLUE"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        if self.__on == True:
            self.__speed = speed

    def isOn(self):
        return self.__on
    def setOn(self, on):
        self.__on = on

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

    def getColor(self):
        return self.__color
    def setColor(self, color):
        if self.__on == True:
            self.__color = color

def main():
    fan = Fan(3, True, 10, "Yellow")
    print("Speed of fan is", fan.getSpeed())
    print("Radius of fan is", fan.getRadius())
    fan.setOn(False)
    print("Fan is On/Off ", fan.isOn())
    print("Color of fan ", fan.getColor())
    fan.setSpeed(1)
    print(fan.getSpeed())

main()