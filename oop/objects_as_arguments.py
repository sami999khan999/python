# objects as arguments:
# This example demonstrates how to modify an attribute of an object in a class using a function.


# Define a class 'Car' with a 'color' attribute
class Car:
    color = None  # The color attribute is initially set to None


# Function to change the color of a car
def change_color(car, color):
    car.color = color  # Modify the car's 'color' attribute


# Create two instances of the 'Car' class
car_1 = Car()
car_2 = Car()

# Call the function to change the color of each car
change_color(car_1, "Red")
change_color(car_2, "Blue")

# Print the color of each car
print(car_1.color)  # Output: Red
print(car_2.color)  # Output: Blue

# Explanation:
# 1. The 'Car' class has an attribute 'color', which is initially set to 'None'.
# 2. The 'change_color' function accepts a 'car' object and a 'color' value, and it modifies the 'color' attribute of the given car.
# 3. We create two instances, 'car_1' and 'car_2', of the 'Car' class.
# 4. We use the 'change_color' function to modify the 'color' of each car object.
# 5. The modified 'color' attribute is printed for both cars, demonstrating that the function successfully changed their attributes.
