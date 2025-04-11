"""
Class with methods that change attributes
"""


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def paint(self, new_color):
        self.color = new_color

    def drive(self):
        print(f"{self.color} {self.brand} is driving!")


if __name__ == '__main__':

    car1 = Car("Range Rover", "White")  # initialize car object
    car1.drive()

    while True :
        choice = input("Do you want to paint your car to a new color (y/n) : ").lower()

        if choice == 'y':
            newColor = input("Enter new color of the car : ")
            car1.paint(newColor)
            car1.drive()
            break
        elif choice == 'n':
            print("Okay 👍")
            car1.drive()
            break
        else:
            print("Invalid input !!")

    print("End of Code")
