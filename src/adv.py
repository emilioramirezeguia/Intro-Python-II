from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Emilio", room["outside"])

# Add items to rooms
room['outside'].add_item(Item("Stick", "Wooden stick."))
room['foyer'].add_item(Item("Rocks", "Not one, but two."))
room['overlook'].add_item(
    Item('Sword', "Shiny. Not like the lightsaber though."))
room['narrow'].add_item(Item("Magic", ""))
room['treasure'].add_item(
    Item("Empty", "No gold. Good for storage maybe?"))

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playing = True
while playing == True:
    print("")
    print(player)
    print("")
    print(player.current_room.description)
    player.print_items()
    player.current_room.print_items()
    print("------------------------------")
    selection = input("""
    What do you want to do now?

    Move somewhere: type 'n' (to go north), 's' (to go south), 'e' (to go east), or 'w' (to go west)

    Grab item: type 'get' or 'take' followed by an item name.
    """).lower().split(" ")

    if len(selection) == 1:
        if selection[0] == "n" or selection[0] == "s" or selection[0] == "e" or selection[0] == "w":
            player.move_to(selection[0])
        elif selection[0] == "q":
            playing = False
            print("Thank you for playing.")
        else:
            print("")
            print("Sorry, that's not a viable direction. Try again")
    elif len(selection) == 2:
        if selection[0] == "get" or selection[0] == "take":
            for item in player.current_room.items:
                if item.name == selection[1].capitalize():
                    player.add_item(item)
                    player.current_room.remove_item(item)
