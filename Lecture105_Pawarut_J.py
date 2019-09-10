class Vehicle:
    licenseCode = ""
    serialcode = ""
    face = ""
    def turnOnAir(self):
        print("Turn On : Air")

class Car(Vehicle):
    def sayhello(self):
        print("Hello")

class Pickup(Vehicle):
    def sayhello(self):
        print("Hello")

class Van(Vehicle):
    def sayhello(self):
        print("Hello")

class Estatecar(Vehicle):
    def sayhello(self):
        print("Hello")

car1 = Car()
car1.turnOnAir()
car1.sayhello()

Pickup1 = Pickup()
Pickup1.turnOnAir()
Pickup1.sayhello()

Van1 = Van()
Van1.turnOnAir()
Van1.sayhello()

estatecar1 = Estatecar()
estatecar1.turnOnAir()
estatecar1.sayhello()