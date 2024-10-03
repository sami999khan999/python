# Multiple Inheritance:
# In multiple inheritance, a class can inherit from more than one parent class.
# The child class will have access to all the attributes and methods of its parent classes.
# In this example, the class 'Fish' inherits from both 'Prey' and 'Predator' classes.


# Base Class: Prey
# The 'Prey' class defines the behavior of animals that flee from predators.
class Prey:
    def __init__(self, name):
        self.name = name  # Each prey has a 'name' attribute (e.g., "Rabbit", "Fish").

    # Method that defines the action of fleeing
    def flee(self):
        print(
            f"This {self.name} flees."
        )  # Prints a message indicating that the prey is fleeing.


# Base Class: Predator
# The 'Predator' class defines the behavior of animals that hunt prey.
class Predator:
    def __init__(self, name):
        self.name = name  # Each predator has a 'name' attribute (e.g., "Lion", "Fish").

    # Method that defines the action of hunting
    def hunt(self):
        print(
            f"This {self.name} hunts."
        )  # Prints a message indicating that the predator is hunting.


# Derived Class: Rabbit
# 'Rabbit' inherits from 'Prey', which means it can flee but does not hunt.
class Rabbit(Prey):
    pass  # Inherits everything from 'Prey' without adding any new behavior.


# Derived Class: Lion
# 'Lion' inherits from 'Predator', which means it can hunt but does not flee.
class Lion(Predator):
    pass  # Inherits everything from 'Predator' without adding any new behavior.


# Derived Class: Fish
# 'Fish' inherits from both 'Prey' and 'Predator', meaning it can both flee and hunt.
# This is an example of multiple inheritance where Fish is both a prey and a predator.
class Fish(Prey, Predator):
    pass  # Inherits methods from both 'Prey' and 'Predator' classes.


# Creating instances and demonstrating multiple inheritance:

# Rabbit instance
rabbit = Rabbit("Rabbit")
rabbit.flee()  # Output: "This Rabbit flees." (inherited from the Prey class)

# Lion instance
lion = Lion("Lion")
lion.hunt()  # Output: "This Lion hunts." (inherited from the Predator class)

# Fish instance (inherits from both Prey and Predator)
fish = Fish("Fish")
fish.flee()  # Output: "This Fish flees." (inherited from the Prey class)
fish.hunt()  # Output: "This Fish hunts." (inherited from the Predator class)

# Explanation of Multiple Inheritance:
# 1. The class 'Fish' inherits from both 'Prey' and 'Predator', so it has access to both the 'flee' method from 'Prey'
#    and the 'hunt' method from 'Predator'. This allows 'Fish' to perform both actions.
# 2. In Python, the method resolution order (MRO) determines which parent class is checked first when a method is called.
#    In this case, the order in which the parent classes are listed (Prey, Predator) is the order in which they are checked.
