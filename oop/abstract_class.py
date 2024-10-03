# Abstract Base Class (ABC):
# An abstract base class is a class that cannot be instantiated on its own and is designed to serve as a blueprint for other classes.
# It is created using the `abc` module and the `ABC` class. Any class inheriting from an abstract base class must implement its abstract methods.
# If a subclass does not implement the abstract methods, it cannot be instantiated.

# Abstract Method:
# An abstract method is a method that is declared, but contains no implementation. Subclasses are forced to implement this method.
# The `@abstractmethod` decorator is used to define abstract methods. In this example, `drive()` and `stop()` are abstract methods in the Vehicle class.

from abc import ABC, abstractmethod


# Abstract Base Class: Vehicle
# 'Vehicle' is an abstract base class that provides a common template for all types of vehicles.
class Vehicle(ABC):
    # Abstract method 'drive', which must be implemented in all subclasses.
    # Abstract methods provide no implementation here and are intended to be overridden by subclasses.
    @abstractmethod
    def drive(self):
        # This method does not provide an implementation, forcing subclasses to define it.
        pass

    # Abstract method 'stop' with a default implementation.
    # The subclass can override this method, but if it doesn't, the parent class implementation will be used.
    @abstractmethod
    def stop(self):
        print("This vehicle is stopped.")


# Concrete Class: Car
# 'Car' is a subclass of 'Vehicle' and provides specific implementations of the abstract methods defined in the parent class.
class Car(Vehicle):
    # Implementing the 'drive' method from the Vehicle class.
    # This method will now have a concrete implementation specific to the Car class.
    def drive(self):
        print("This car is driving.")

    # Overriding the 'stop' method to provide a specific implementation for the Car class.
    def stop(self):
        print("This car is stopped.")


# Concrete Class: Bike
# 'Bike' is another subclass of 'Vehicle' and provides its own implementation of the abstract methods.
class Bike(Vehicle):
    # Implementing the 'drive' method specifically for the Bike class.
    def drive(self):
        print("This bike is driving.")

    # Overriding the 'stop' method for the Bike class.
    def stop(self):
        print("This bike is stopped.")


# Demonstrating the use of the Car class.
# Since 'Car' implements the abstract methods of 'Vehicle', it can be instantiated and used.
car = Car()
car.drive()  # Output: This car is driving.
car.stop()  # Output: This car is stopped.

# Demonstrating the use of the Bike class.
# 'Bike' also provides concrete implementations of the abstract methods, so it can be instantiated.
bike = Bike()
bike.drive()  # Output: This bike is driving.
bike.stop()  # Output: This bike is stopped.


# Key points:
# 1. Abstract base classes enforce that child classes must implement certain methods, providing a consistent interface.
# 2. Abstract methods have no implementation in the parent class and must be overridden in the child classes.
# 3. The @abstractmethod decorator is used to define abstract methods in the parent class.
# 4. If a subclass fails to implement all abstract methods, it will not be instantiable, ensuring proper method implementation across subclasses.
# 5. ABCs allow for defining default behaviors that child classes can choose to override.
