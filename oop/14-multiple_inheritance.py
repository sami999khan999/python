# Multiple Inheritance Example:
# In multiple inheritance, a class can inherit attributes and methods from more than one parent class.
# This example shows how the Fish class can inherit behaviors from both Prey and Predator,
# allowing it to both flee and hunt.


# Base Class: Prey
# Represents animals that have the ability to flee.
class Prey:
    def __init__(self, name):
        self.name = name  # Each Prey instance has a name.

    def flee(self):
        # Method representing the action of fleeing.
        print(f"This {self.name} flees.")


# Base Class: Predator
# Represents animals that have the ability to hunt.
class Predator:
    def __init__(self, name):
        self.name = name  # Each Predator instance has a name.

    def hunt(self):
        # Method representing the action of hunting.
        print(f"This {self.name} hunts.")


# Derived Class: Rabbit
# Inherits from Prey, so it only has the fleeing behavior.
class Rabbit(Prey):
    pass  # Inherits everything from Prey without modification.


# Derived Class: Lion
# Inherits from Predator, so it only has the hunting behavior.
class Lion(Predator):
    pass  # Inherits everything from Predator without modification.


# Derived Class: Fish
# Inherits from both Prey and Predator, thus gaining both behaviors.
class Fish(Prey, Predator):
    pass  # Inherits methods from both Prey and Predator.


# Creating instances to demonstrate multiple inheritance:

# Create a Rabbit instance and call its flee method.
rabbit = Rabbit("Rabbit")
rabbit.flee()  # Output: "This Rabbit flees."

# Create a Lion instance and call its hunt method.
lion = Lion("Lion")
lion.hunt()  # Output: "This Lion hunts."

# Create a Fish instance, which inherits from both Prey and Predator.
fish = Fish("Fish")
fish.flee()  # Output: "This Fish flees." (from Prey)
fish.hunt()  # Output: "This Fish hunts." (from Predator)

# Explanation:
# 1. The Fish class inherits from both Prey and Predator, so it has access to the flee() method (from Prey)
#    and the hunt() method (from Predator).
# 2. Python uses the Method Resolution Order (MRO) to determine which parent class is searched first when
#    a method is called. In this case, the order is determined by the class declaration: Fish(Prey, Predator).
# 3. This means that if there were methods with the same name in both parent classes, Python would use the method
#    from Prey first, then Predator.

# Summary:
# - Multiple inheritance enables a class to inherit behaviors from more than one parent class.
# - The Fish class, as an example, can both flee and hunt because it inherits from Prey and Predator.
# - The Method Resolution Order (MRO) determines the sequence in which base classes are searched for methods.
