class Item:
    def __init__(self, name: str, price: float, quantity: int):
        # Type Annotations:
        # - name is expected to be a string.
        # - price is expected to be a float.
        # - quantity is expected to be an integer.

        # Assertions:
        # These checks ensure that the input values are valid.
        # The price must be zero or a positive value.
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        # The quantity must also be zero or a positive value.
        assert (
            quantity >= 0
        ), f"Quantity {quantity} is not greater than or equal to zero!"

        # Setting instance variables.
        self.name = name
        self.price = price
        self.quantity = quantity


# OBJECT CREATION:
# Attempting to create an Item with a negative quantity will trigger an assertion error.
item1 = Item("Phone", 200, -1)
# This will raise an AssertionError due to quantity being -1.

item2 = Item("Laptop", 800, 3)

print(item1.price)

# Summary:
# - **Type Annotations:** Specify the expected data types for each parameter, helping with readability and error checking.
# - **Assertions:** Verify that certain conditions (non-negative price and quantity) hold true.
#   If an assertion fails, an AssertionError is raised with a descriptive message.
# - This design helps catch invalid input early, ensuring that only valid Item objects are created.
