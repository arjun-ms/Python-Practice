class Vehicle:

    def __init__(self,name,max_speed,milege):
        self.name = name
        self.max_speed = max_speed
        self.milege = milege

    def seating_capacity(self,capacity):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")

class Bus(Vehicle):
    def seating_capacity(self,capacity=50):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")

Tesla = Vehicle("Model X",500,50)
print(f"Max speed: {Tesla.max_speed}")
print(f"Milege: {Tesla.milege}")
Tesla.seating_capacity(4)

Ksrtc = Bus("TVM",100,25)
print(f"Max speed: {Ksrtc.max_speed}")
print(f"Milege: {Ksrtc.milege}")
Ksrtc.seating_capacity(100)