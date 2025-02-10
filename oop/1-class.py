# A class is a blueprint for creating objects (instances) with specific attributes and behaviors.
# It defines the structure (attributes) and methods (behavior) that the objects will have.


class Car:
    # Car class defines a blueprint for car objects.

    # Attributes:
    # - make: Car manufacturer (e.g., Chevy, Ford)
    # - model: Car model (e.g., Corvette, Mustang)
    # - year: Car manufacture year
    # - color: Car color

    # Methods:
    # - drive: Simulates the car driving
    # - stop: Simulates the car stopping

    # __init__ initializes a new object with specific attributes.
    def __init__(self, make, model, year, color):
        # 'self' refers to the instance, attaching values to it.
        self.make = make  # Car make
        self.model = model  # Car model
        self.year = year  # Car year
        self.color = color  # Car color

    # Simulates driving the car.
    def drive(self):
        print(f"This {self.model} is driving")  # Accesses model and prints message.

    # Simulates stopping the car.
    def stop(self):
        print(f"This {self.model} is stopping")  # Accesses model and prints message.


# OBJECT CREATION (Instances): Instances of Car class with specific attributes.
car_1 = Car("Chevy", "Corvette", 2021, "Black")  # Creates car_1 with attributes
car_2 = Car("Ford", "Mustang", 2022, "Black")  # Creates car_2 with attributes

# Accessing car_1's attributes.
print(car_1.make)  # Chevy
print(car_1.model)  # Corvette
print(car_1.year)  # 2021
print(car_1.color)  # Black

# Calling methods on car_1.
car_1.drive()  # This Corvette is driving
car_1.stop()  # This Corvette is stopping

# Calling methods on car_2.
car_2.drive()  # This Mustang is driving
car_2.stop()  # This Mustang is stopping

# Summary:
# - A class defines the structure (attributes) and behavior (methods) of objects.
# - Objects (instances) are created from the class with unique attribute values.
# - The '__init__' method initializes the object when created.
# - Methods define behaviors and can be called on objects.
# - 'self' refers to the current instance, allowing access to attributes and methods.
