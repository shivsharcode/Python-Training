"""
simple class with attributes and methods.
"""


class Car:
    # constructor
    def __init__(self, brand, color):
        self.brand = brand  # attribute
        self.color = color  # attribute

    # method
    def drive(self):
        print(f"{self.color} {self.brand} is driving ! ")


# create objects (instances of Car)
car1 = Car("Tata", "Blue")
car2 = Car("Honda", "Black")

# call methods
car1.drive()
car2.drive()



