class Character:
    hp = 100  # Class variable: 'hp' is defined here. It's shared by all instances of this class unless changed within an instance.

    # __init__ is the constructor method that's called when a new object (or instance) of the class is created.
    # It initializes (or sets) the instance variables for that particular object.
    def __init__(self, weapon, amo, heal):
        # 'self' refers to the current object (or instance) being created.
        # Instance variables are created here. Each object will have its own 'weapon', 'amo', and 'heal' values.
        self.weapon = weapon  # Assign the value passed to the 'weapon' parameter to the instance variable 'self.weapon'.

        self.amo = amo  # Assign the value passed to the 'amo' parameter to the instance variable 'self.amo'.

        self.heal = heal  # Assign the value passed to the 'heal' parameter to the instance variable 'self.heal'.

    # This method is used to display (or print) the player's statistics.
    # It accesses both class variables (like 'hp') and instance variables (like 'weapon', 'amo', and 'heal').
    def statistics(self):
        # 'self.hp' refers to the object's 'hp' value, which is either the class variable or an overridden value.
        # The instance variables ('self.weapon', 'self.amo', 'self.heal') refer to the values specific to this object.
        print(
            f"This player has {self.hp} hp, {self.amo} amo and has {self.heal} healing items. And he's using {self.weapon}"
        )


# Create a new instance of the 'Character' class named 'player'.
# The 'player' object gets its own 'weapon', 'amo', and 'heal' values based on what's passed to the constructor.
player = Character(
    "M416", 240, 3
)  # 'player' has a weapon "M416", 240 ammo, and 3 healing items.

# Call the 'statistics' method on 'player' to print the player's stats.
# The method will print: "This player has 100 hp, 240 amo and has 3 healing items. And he's using M416".
# Here, 'self.hp' refers to the class variable 'hp' (100), since 'player' hasn't overridden it.
player.statistics()

# Create another instance of the 'Character' class named 'player2'.
# The 'player2' object gets its own 'weapon', 'amo', and 'heal' values as well.
player2 = Character(
    "AWM", 19, 6
)  # 'player2' has a weapon "AWM", 19 ammo, and 6 healing items.

# Override the 'hp' value for 'player2' by directly setting it.
# This changes 'player2.hp' from the default class value (100) to 75, but only for 'player2'.
# 'player' still has 100 hp.
player2.hp = 75

# Call the 'statistics' method on 'player2' to print the player's stats.
# The method will print: "This player has 75 hp, 19 amo and has 6 healing items. And he's using AWM".
# Here, 'self.hp' refers to the overridden value (75) for 'player2'.
player2.statistics()
