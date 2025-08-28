# Activity 2: Polymorphism Challenge! 

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return("Driving")

class Plane(Vehicle):
    def move(self):
        return("Flying")


# Polymorphism in action

for vehicles in [Car(), Plane()]:
    print(vehicles.move())