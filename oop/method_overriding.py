# Method Overriding:
# Method overriding occurs when a subclass (child class) provides a specific implementation of a method
# that is already defined in its parent class. The child class's method overrides (replaces) the parent
# class's method, allowing for specialized behavior in the subclass.


# Base Class: Animal
# The Animal class defines a common 'eat' method that all animals inherit by default.
class Animal:
    def __init__(self, name):
        self.name = name  # Each animal has a 'name' attribute.

    # This 'eat' method is defined in the parent class (Animal).
    def eat(self):
        print(
            f"{self.name} is eating grass."
        )  # The generic behavior for eating is described here.


# Subclass: Rabbit
# The Rabbit class inherits from Animal but overrides the 'eat' method to provide more specific behavior.
class Rabbit(Animal):
    # This 'eat' method in the Rabbit class overrides the 'eat' method from the Animal class.
    def eat(self):
        print(f"{self.name} is eating.")  # More specific behavior for Rabbit.


# Creating an instance of Rabbit:
rabbit = Rabbit("Rabbit")

# Calling the 'eat' method:
rabbit.eat()  # Output: "Rabbit is eating." (This calls the overridden 'eat' method in the Rabbit class, not the one in Animal)

# Explanation of Method Overriding:
# 1. The 'eat' method in the Rabbit class replaces the 'eat' method in the Animal class.
# 2. When the 'eat' method is called on a Rabbit object, Python uses the Rabbit class's method instead of the Animal class's method.
# 3. This allows subclasses to have behavior that is more specific or specialized than their parent classes.
