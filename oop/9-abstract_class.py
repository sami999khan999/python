from abc import ABC, abstractmethod


# Abstract Base Class: Vehicle
# This class serves as a blueprint for all vehicle types.
# It cannot be instantiated directly because it contains abstract methods.
class Vehicle(ABC):
    # Abstract method: drive
    # This method is declared but not implemented here.
    # Any subclass inheriting Vehicle must provide its own implementation of drive.
    @abstractmethod
    def drive(self):
        # No implementation here; this method must be overridden in the subclass.
        pass

    # Abstract method: stop
    # Although marked abstract, a default implementation is provided.
    # Subclasses can override this default behavior if needed.
    @abstractmethod
    def stop(self):
        print("This vehicle is stopped.")


# Concrete Class: Car
# Car is a subclass of Vehicle and provides concrete implementations of the abstract methods.
class Car(Vehicle):
    # Implementing the drive method for Car.
    def drive(self):
        print("This car is driving.")

    # Overriding the stop method for Car.
    def stop(self):
        print("This car is stopped.")


# Concrete Class: Bike
# Bike is another subclass of Vehicle, with its own implementations.
class Bike(Vehicle):
    # Implementing the drive method for Bike.
    def drive(self):
        print("This bike is driving.")

    # Overriding the stop method for Bike.
    def stop(self):
        print("This bike is stopped.")


# Demonstration of instantiating and using the concrete classes:

# Create a Car object.
# Since Car implements all abstract methods, it can be instantiated.
car = Car()
car.drive()  # Expected Output: "This car is driving."
car.stop()  # Expected Output: "This car is stopped."

# Create a Bike object.
# Bike also provides its own implementations, so instantiation is allowed.
bike = Bike()
bike.drive()  # Expected Output: "This bike is driving."
bike.stop()  # Expected Output: "This bike is stopped."

# Summary:
# - Abstract Base Classes (ABCs) provide a common template for subclasses.
# - ABCs contain abstract methods that must be implemented by any concrete subclass.
# - The @abstractmethod decorator enforces that subclasses override the abstract methods.
# - If a subclass does not implement all abstract methods, it cannot be instantiated.
# - Default behavior can be provided in abstract methods (as seen in stop), but subclasses are free to override.
