# OOP

class Car:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count
        print("Mashina qismi tayyor!")

class Plane:
    def __init__(self, wing_span):
        self.wing_span = wing_span
        print("Samolyot qismi tayyor!")

class FlyingCar(Car, Plane):
    def __init__(self, wheel_count, wing_span, brand):
        # 1. Mashina qismini yig'amiz
        Car.__init__(self, wheel_count)
        
        # 2. Samolyot qismini yig'amiz
        Plane.__init__(self, wing_span)
        
        # 3. O'zimizning yangi atributimiz
        self.brand = brand
        print(f"{self.brand} uchar mashinasi to'liq tayyor!")