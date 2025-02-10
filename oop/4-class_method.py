class Product:
    # CLASS VARIABLE: Shared by all instances of the Product class.
    tax_rate = 0.1

    def __init__(self, name, price):
        # INSTANCE VARIABLES: Specific to each product instance.
        self.name = name
        self.price = price

    def calculate_price(self, quantity):
        # Calculates the total price including tax for a given quantity.
        # Uses the class variable 'tax_rate' in the calculation.
        return (self.price + self.price * self.tax_rate) * quantity

    @classmethod
    def set_tax_rate(cls, new_rate):
        # CLASS METHOD: This method takes the class (cls) as its first argument.
        # It can modify class variables that affect all instances.
        cls.tax_rate = new_rate  # Updates the tax_rate for all Product instances.


# Creating two Product instances.
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)

# Using the class method to change the tax_rate for all instances.
Product.set_tax_rate(0.2)

# The new tax_rate (0.2) is now used in the price calculation.
print(
    product1.calculate_price(1)
)  # Calculates price for 1 Laptop with the updated tax rate.

# Summary:
# - A class method is defined with the @classmethod decorator.
# - It receives the class (cls) as the first parameter instead of an instance (self).
# - Clanss methods ca access and modify class variables, affecting all instances.
# - In this example, the set_tax_rate() class method updates the tax_rate for all Product objects.
