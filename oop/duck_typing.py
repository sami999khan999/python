# Duck Typing in Python:
# Duck typing is a concept where an object's behavior is more important than its actual class or type.
# If an object implements the required methods, it can be used in place of another object, regardless of its class.
# The name comes from the saying "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
# This concept allows for greater flexibility in writing code, as it focuses on behavior rather than explicit inheritance or type checking.

# Example: We create two classes, Duck and Chicken, both of which have 'walk' and 'talk' methods.


class Duck:
    name = "Duck"  # Class attribute: All Duck instances share this name

    def walk(self):
        # This method prints how a duck walks.
        # It shows that a Duck can "walk," which fulfills part of the required behavior for duck typing.
        print(
            f"This {self.name} is walking."
        )  # Output will say that a Duck is walking.

    def talk(self):
        # This method prints the sound a duck makes.
        # It shows that a Duck can "talk" (quack), which is another behavior we expect from a duck.
        print(
            f"This {self.name} is quacking."
        )  # Output will say that a Duck is quacking.


class Chicken:
    name = "Chicken"  # Class attribute: All Chicken instances share this name

    def walk(self):
        # Like Duck, Chicken also has a 'walk' method.
        # This demonstrates that a Chicken can also "walk," just like a Duck, making it compatible with duck typing.
        print(
            f"This {self.name} is walking."
        )  # Output will say that a Chicken is walking.

    def talk(self):
        # Like Duck, Chicken also has a 'talk' method.
        # This method demonstrates that a Chicken can "talk" (cluck), fulfilling the behavior needed for duck typing.
        print(
            f"This {self.name} is clucking."
        )  # Output will say that a Chicken is clucking.


# The Person class below demonstrates duck typing. It expects any object passed to its 'catch' method to have 'walk' and 'talk' methods.
class Person:
    def catch(self, bird):
        # This method doesn't check whether 'bird' is a Duck or a Chicken.
        # It simply calls the 'walk' and 'talk' methods on the object passed, assuming it has those methods.
        bird.talk()  # Calls the object's 'talk' method (either quack or cluck depending on the object).
        bird.walk()  # Calls the object's 'walk' method.


# Creating instances of Duck and Chicken.
duck = Duck()  # Creating an instance of Duck with name "Duck".
chicken = Chicken()  # Creating an instance of Chicken with name "Chicken".

# Creating an instance of Person who will interact with both the Duck and Chicken.
person = Person()

# Demonstrating duck typing: the person doesn't need to know whether they are interacting with a Duck or Chicken,
# they just expect the object to "talk" and "walk."

# Calling the 'catch' method with a Duck instance.
# Since Duck has 'talk' (quack) and 'walk', this works as expected.
person.catch(duck)
# Output:
# "This Duck is quacking."
# "This Duck is walking."

# Calling the 'catch' method with a Chicken instance.
# Since Chicken also has 'talk' (cluck) and 'walk', this works as expected too.
person.catch(chicken)
# Output:
# "This Chicken is clucking."
# "This Chicken is walking."

# Key points:
# 1. The 'Person' class uses duck typing by expecting any object passed to its 'catch' method to have the methods 'talk' and 'walk'.
# 2. Neither Duck nor Chicken inherit from a common class like 'Bird'—yet, they can both be used in the 'Person' class.
# 3. This flexibility makes code more versatile, as we can pass any object that implements the right methods, even if it's a completely different class.
