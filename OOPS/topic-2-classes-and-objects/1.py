"""
Class : A class is a blueprint or template to create objects.

Object : An object is an instance of a class, it represents a real-world entity
An object has - attributes and behaviours(methods)
When you create an object, the compiler/interpreter allocate memory and initialize it
"""


class Car:
    pass  # empty class for now


if __name__ == '__main__':
    print("OOPs")
    myCar = Car()
    print(myCar)
    print(type(myCar))


