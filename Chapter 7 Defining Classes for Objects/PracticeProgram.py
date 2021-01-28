class A:
    def A(self):
        self.radius = 3
        return self.radius
    radius = 5
obj = A()
print(obj.radius)
print(obj.A())

class B:
    def __init__(self):
        self.radius = 90
    def setRadius(self):
        self.radius = self.radius
        return self.radius
obj1 = B()
print(obj1.setRadius())