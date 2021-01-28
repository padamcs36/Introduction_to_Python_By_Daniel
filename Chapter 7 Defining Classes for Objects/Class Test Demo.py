class Robot:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
    def self_description(self):
        print("Car name is {} and Model is {} and Color is {}".format(self.name, self.model, self.color))

object = Robot("Mehran", 2020, "Pink")
object.self_description()