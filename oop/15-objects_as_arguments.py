# This example demonstrates how objects can be passed as arguments to functions
# and have their attributes modified directly.


# Define a Car class with a 'color' attribute.
class Car:
    # The 'color' attribute is initially set to None.
    # Note: In a real-world scenario, you might define instance attributes in an __init__ method.
    color = None


# Define a function that accepts a Car object and a new color.
def change_color(car, new_color):
    # Modify the car object's 'color' attribute to the provided new color.
    car.color = new_color


# Create two instances of the Car class.
car_1 = Car()
car_2 = Car()

# Use the function to change the color of each car.
change_color(car_1, "Red")
change_color(car_2, "Blue")

# Print the color of each car to verify that the attribute has been updated.
print(car_1.color)  # Output: Red
print(car_2.color)  # Output: Blue

# Summary:
# - The Car class has a 'color' attribute that can be modified.
# - The change_color function takes a car object and a new color, then updates the car's color.
# - By passing objects as arguments, we can directly modify their internal state.
