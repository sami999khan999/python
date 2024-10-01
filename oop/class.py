# A class is a blueprint or template for creating objects (instances).
# Classes allow us to group data (attributes) and behavior (methods) into a single unit.
# In essence, a class defines the structure and behavior that the objects (instances) will have.


class Car:
    # The Car class represents a template for creating car objects.

    # Attributes:
    # - make: The brand or manufacturer of the car (e.g., Chevy, Ford)
    # - model: The model of the car (e.g., Corvette, Mustang)
    # - year: The manufacture year of the car
    # - color: The color of the car

    # Methods:
    # - drive: A method that simulates driving the car
    # - stop: A method that simulates stopping the car

    # The __init__ method is a constructor that initializes a new instance of the class.
    # It runs automatically when a new object of the class is created.
    def __init__(self, make, model, year, color):

        # The __init__ method initializes the Car object with four attributes:
        # - make: This instance of the Car object's manufacturer (e.g., 'Chevy')
        # - model: This instance of the Car object's model (e.g., 'Corvette')
        # - year: This instance of the Car object's year (e.g., 2021)
        # - color: This instance of the Car object's color (e.g., 'Black')

        # The 'self' parameter refers to the current instance of the class.
        # It allows us to attach these attributes to the specific object being created.

        # 'self.make', 'self.model', etc. refer to the instance variables.
        # These are specific to the object created from the class and store data.

        self.make = make  # Assigns the 'make' of the car to the object
        self.model = model  # Assigns the 'model' of the car to the object
        self.year = year  # Assigns the 'year' of the car to the object
        self.color = color  # Assigns the 'color' of the car to the object

    # This is a method (a function inside a class) that defines behavior for the Car object.
    def drive(self):
        # The drive method prints a message indicating that the car is driving.
        # The 'self' parameter allows us to access the object's attributes within the method.
        print(f"This {self.model} is driving")

    # Another method that defines a different behavior for the Car object.
    def stop(self):
        # The stop method prints a message indicating that the car is stopping.
        print(f"This {self.model} is stopping")


# When we create a new object from the class, the __init__ method is automatically called.
# This process is called instantiation.
car_1 = Car(
    "Chevy", "Corvette", "2021", "Black"
)  # Creates an instance (object) of the Car class

car_2 = Car(
    "Ford", "Mustang", "2022", "Black"
)  # Creates another instance (object) of the Car class

# car_1 and car_2 are now objects (or instances) of the Car class.
# Each object has its own set of attributes (make, model, year, color), specific to that object.

# Accessing and printing the attributes of the car_1 object.
print(car_1.make)  # Output: Chevy (Gets the 'make' of car_1)
print(car_1.model)  # Output: Corvette (Gets the 'model' of car_1)
print(car_1.year)  # Output: 2021 (Gets the 'year' of car_1)
print(car_1.color)  # Output: Black (Gets the 'color' of car_1)

# Calling the methods (drive and stop) on the car_1 object.
car_1.drive()  # Output: This Corvette is driving (Simulates driving)
car_1.stop()  # Output: This Corvette is stopping (Simulates stopping)

# Similarly, we can call methods on car_2 object.
car_2.drive()  # Output: This Mustang is driving
car_2.stop()  # Output: This Mustang is stopping

# In summary:
# - A class defines the structure (attributes) and behavior (methods) for objects.
# - An object is an instance of a class, with its own unique attributes.
# - The 'self' keyword allows each object to refer to its own attributes and methods.
# - We can create multiple objects from the same class, and each object can have different values for its attributes.
