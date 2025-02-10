# Method Overriding Example:
# Method overriding allows a subclass to provide its own implementation of a method that is already defined
# in its parent class. The subclass's version of the method will be used when called on an instance of the subclass.


# Base Class: Animal
# The Animal class defines a general 'eat' method that provides a generic eating behavior.
class Animal:
    def __init__(self, name):
        self.name = name  # Every animal has a name.

    def eat(self):
        # This is the generic eating behavior defined in the parent class.
        print(f"{self.name} is eating grass.")


# Subclass: Rabbit
# The Rabbit class inherits from Animal and overrides the 'eat' method to provide behavior specific to rabbits.
class Rabbit(Animal):
    def eat(self):
        # This method overrides the Animal class's 'eat' method.
        # When a Rabbit object calls 'eat', this method is executed instead of the parent class's version.
        print(f"{self.name} is eating.")


# Creating an instance of Rabbit.
rabbit = Rabbit("Rabbit")

# Calling the 'eat' method on the Rabbit instance.
# Even though the Animal class defines an 'eat' method, the Rabbit class's override is used.
rabbit.eat()  # Output: "Rabbit is eating."


# Summary:
# - Method overriding allows subclasses to modify or completely replace the behavior of methods inherited from a parent class.
# - When a method is called on an object, Python checks for an overriding method in the object's class.
# - This enables more specific behavior in subclasses while still retaining a common interface defined by the parent class.
