# random module

# The random module in Python provides functions to generate random numbers, select random elements, and perform other operations that require randomness. It's widely used in simulations, gaming, or any scenario where randomness is needed.

import random

# ===================================================================================================== #

# random.random()

# Generates a random floating-point number between 0.0 and 1.0.

x = random.random()

print(x)

# ===================================================================================================== #

# randint()

# Returns a random integer between a and b (both inclusive).

y = random.randint(1, 10)

print(y)

# ===================================================================================================== #

# randrange()

# Returns a randomly selected element from the range created by start, stop, and step.

z = random.randrange(0, 10, 2)

print(z)

# ===================================================================================================== #

# choice()

# Returns a random element from a non-empty sequence (like a list or string).

name = ["Alice", "Bob", "Charlie"]

person = random.choice(name)

print(person)

# ===================================================================================================== #

# choices()

# Returns a list of k random elements from the population. You can also assign weights to control the probability of each element being picked.

numbers = [1, 2, 3, 4, 5]

chosen_numbers = random.choices(numbers, k=3)

print(chosen_numbers)

# ===================================================================================================== #

# shuffle()

# Shuffles the sequence x in place (mutates the sequence).

deck = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(deck)

print(deck)
