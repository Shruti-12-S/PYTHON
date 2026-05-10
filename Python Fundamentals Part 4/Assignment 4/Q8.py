'''Concept: Instance & Class Attributes
Create a class Player with:
    • a class variable player_count
    • instance variables name and level 
Track how many players were created.
'''

# Class Player
class Player:

    # Class variable
    player_count = 0

    def __init__(self, name, level):
        # Instance variables
        self.name = name
        self.level = level

        # Increase player count whenever a new object is created
        Player.player_count += 1

    def display(self):
        print("Player Name :", self.name)
        print("Player Level:", self.level)


# Creating objects
p1 = Player("Rahul", 5)
p2 = Player("Aman", 8)
p3 = Player("Priya", 10)

# Display player details
p1.display()
print()

p2.display()
print()

p3.display()
print()

# Display total number of players created
print("Total Players Created:", Player.player_count)
