# Method Chaining Example:
# Method chaining allows multiple methods to be called on the same object in one line.
# Each method returns the object itself (self), so the next method can be called immediately.
# This creates a fluent interface that makes the code concise and easy to read.


class Car:
    # The Car class simulates various actions a car can perform.

    def start(self):
        # Simulate starting the car.
        print("Start the car...")
        # Returning self allows the next method to be chained.
        return self

    def drive(self):
        # Simulate driving the car.
        print("Drive the car...")
        # Return self to allow further chaining.
        return self

    def brake(self):
        # Simulate braking the car.
        print("Brake the car...")
        # Return self so more methods can be chained after this.
        return self

    def stop(self):
        # Simulate stopping the car.
        print("Stop the car...")
        # Return self to complete the chain (even if no further calls follow).
        return self


# Creating an instance of Car.
car = Car()

# Demonstrate method chaining:
# Each method call returns the car instance, enabling the next method to be called immediately.
car.start().drive().brake().stop()

# Expected Output:
# Start the car...
# Drive the car...
# Brake the car...
# Stop the car...

# Summary:
# - Method chaining improves code readability by allowing multiple method calls on a single line.
# - Each method must return 'self' so that the subsequent method in the chain can be invoked.
# - This fluent interface pattern is useful for writing concise code where an object's state is modified
#   or actions are performed in sequence.
