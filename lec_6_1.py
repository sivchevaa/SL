import math

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def find_hypotenuse(self):
        self.c = math.sqrt(self.a * self.a + self.b * self.b)
        print(f"The hypotemuse is {self.c}")

    def area(self):
        self.area = (self.a * self.b) / 2
        print(f"The area is {self.area}")

    def perimeter(self):
        self.p = self.a + self.b + self.c
        print(f"The perimeter is {self.p}")

toshko = Triangle(6.0, 8.0)
toshko.find_hypotenuse()
toshko.area()
toshko.perimeter()