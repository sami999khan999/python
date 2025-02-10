# This example demonstrates the use of @property and @property.setter
# to encapsulate and control access to private attributes of a class.


class Rectangle:
    def __init__(self, width: float, height: float):
        # Initialize the rectangle with width and height.
        # These attributes are private, indicated by the double underscore prefix.
        self.__width = width
        self.__height = height

    @property
    def width(self):
        # Getter for the width.
        # This method allows external code to access the private __width attribute.
        # Using @property makes this method behave like a read-only attribute.
        return self.__width

    @width.setter
    def width(self, value: float):
        # Setter for the width.
        # This method allows external code to modify the private __width attribute.
        # It includes validation to ensure that the width is a positive number.
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self.__width = value  # Update the private attribute if the value is valid.

    @property
    def height(self):
        # Getter for the height.
        # This provides read access to the private __height attribute.
        return self.__height

    @height.setter
    def height(self, value: float):
        # Setter for the height.
        # It validates that the new value is positive before updating the private attribute.
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self.__height = value  # Update the private attribute if the value is valid.

    @property
    def area(self):
        # Computed property for the area.
        # This property calculates the area based on the current width and height.
        return self.__width * self.__height

    @property
    def perimeter(self):
        # Computed property for the perimeter.
        # This calculates the perimeter using the current width and height.
        return 2 * (self.__width + self.__height)


# Example Usage:
rect = Rectangle(5, 10)
# Access the width and height using the getters.
print("Width:", rect.width)  # Output: 5
print("Height:", rect.height)  # Output: 10

# Access computed properties.
print("Area:", rect.area)  # Output: 50 (5 * 10)
print("Perimeter:", rect.perimeter)  # Output: 30 (2 * (5 + 10))

# Update the width using the setter, which validates the input.
rect.width = 15
print("Updated Width:", rect.width)  # Output: 15
# The area property is recalculated using the new width.
print("Updated Area:", rect.area)  # Output: 150 (15 * 10)

# Attempt to set an invalid height, which will trigger a ValueError.
try:
    rect.height = -5
except ValueError as e:
    print(e)  # Output: Height must be a positive number.

# Summary:
# - @property is used to create getter methods that allow access to private attributes.
# - @<property>.setter is used to define setter methods with validation,
#   enabling controlled modifications of these attributes.
# - Computed properties like 'area' and 'perimeter' provide dynamic calculations
#   based on the current state of the object.
# - This approach encapsulates internal data and ensures that it is only modified
#   in a controlled, validated manner.
