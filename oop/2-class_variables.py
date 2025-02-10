class Character:
    # CLASS VARIABLE: Shared by all instances of the class unless overridden.
    hp = 100  # Default HP for all characters.

    def __init__(self, weapon, amo, heal):
        # INSTANCE VARIABLES: Unique to each object.
        self.weapon = weapon  # Weapon specific to the character.
        self.amo = amo  # Ammo specific to the character.
        self.heal = heal  # Healing items specific to the character.

    def statistics(self):
        # Accessing both class and instance variables.
        print(
            f"This player has {self.hp} HP, {self.weapon} weapon, {self.amo} ammo, and {self.heal} healing items."
        )


# OBJECT CREATION: Instances inherit the class variable 'hp' by default.
player1 = Character("M416", 240, 3)
player1.statistics()  # Displays player1's stats.

# Creating another instance. Inherits default 'hp'.
player2 = Character("AWM", 19, 6)
player2.statistics()  # Displays player2's stats.

# OVERRIDING CLASS VARIABLE: player2 has custom HP.
player2.hp = 75  # player2's HP is now 75 instead of the default 100.
player2.statistics()  # Displays player2's updated stats.

# Summary:
# - CLASS VARIABLES are shared across all instances by default.
# - You can OVERRIDE class variables for individual instances.
# - INSTANCE METHODS can access both class and instance variables.
