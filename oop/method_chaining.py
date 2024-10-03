# Method Chaining:
# Method chaining allows multiple methods to be called on the same object in a single line.
# Each method call returns the object itself, allowing the next method to be called immediately after.
# This creates a fluent interface, improving code readability and conciseness.


# Class: Car
# The Car class contains methods that represent different actions a car can perform.
class Car:
    # The 'start' method prints a message and returns 'self', enabling method chaining.
    def start(self):
        print("Start the car...")
        return (
            self  # Returning 'self' allows the next method in the chain to be called.
        )

    # The 'drive' method prints a message and returns 'self' for chaining.
    def drive(self):
        print("Drive the car...")
        return self  # Returning 'self' for chaining.

    # The 'brake' method prints a message and returns 'self' for chaining.
    def brake(self):
        print("Brake the car...")
        return self  # Returning 'self' for chaining.

    # The 'stop' method prints a message and returns 'self' for chaining.
    def stop(self):
        print("Stop the car...")
        return self  # Returning 'self' for chaining.


# Creating an instance of Car:
car = Car()

# Using method chaining to call multiple methods in a single statement:
car.start().drive().brake().stop()

# Output:
# Start the car...
# Drive the car...
# Brake the car...
# Stop the car...

# Explanation of Method Chaining:
# 1. Each method (start, drive, brake, stop) returns 'self', which is the current instance of the Car class.
# 2. By returning 'self', we can call another method immediately after the previous method, creating a chain of method calls.
# 3. In this example, 'start' is called first, then 'drive', followed by 'brake', and finally 'stop', all on the same 'car' object.
# 4. This approach simplifies the code, making it more readable and elegant compared to calling each method on a separate line.
