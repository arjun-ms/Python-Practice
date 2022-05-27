class Vehicle:
    # class attribute
    color = "White"

    def __init__(self,name,max_speed,milege,capacity):
        self.name = name
        self.max_speed = max_speed
        self.milege = milege
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    # def seating_capacity(self,capacity):
    #     print(f"The seating capacity of a {self.name} is {capacity} passengers")


class Bus(Vehicle):

    # def seating_capacity(self,capacity=50):
    #     print(f"The seating capacity of a {self.name} is {capacity} passengers")
    def fare(self):
        amount = super().fare()
        amount = amount *10/100
        return amount
        



Tesla = Vehicle("Model X",500,50,4)
print(f"Max speed: {Tesla.max_speed}")
print(f"Milege: {Tesla.milege}")
# Tesla.seating_capacity(4)
print(Tesla.color)
print(f"Amt: {Tesla.fare()}")

Ksrtc = Bus("TVM",100,25,50)
print(f"Max speed: {Ksrtc.max_speed}")
print(f"Milege: {Ksrtc.milege}")
# Ksrtc.seating_capacity(100)
print(Ksrtc.color)
print(f"Amt: {Ksrtc.fare()}")

# checking type
print(type(Ksrtc))

# checking Instance type
print(isinstance(Ksrtc,Vehicle))