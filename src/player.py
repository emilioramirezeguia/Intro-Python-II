# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        if items == None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"Name: {self.name}, Current Room: {self.current_room}"

    def __repr__(self):
        return f"Player({self.name}, {self.current_room})"

    # Play should take directions and move
    def move_to(self, direction):
        # Do a sort of switch statement / multiple if statement
        if direction == 'n':
            # Check if player can move to that direction. So check if there is a north attribute for that room.
            # If there is, move the player there, so reassign current_room value. If there is not, print error message.
            if self.current_room.n_to != None:
                self.current_room = self.current_room.n_to
            else:
                print("")
                print("Oops, there's no room there.")
        elif direction == 's':
            if self.current_room.s_to != None:
                self.current_room = self.current_room.s_to
            else:
                print("")
                print("Oops, there's no room there.")
        elif direction == 'e':
            if self.current_room.e_to != None:
                self.current_room = self.current_room.e_to
            else:
                print("")
                print("Oops, there's no room there.")
        elif direction == 'w':
            if self.current_room.w_to != None:
                self.current_room = self.current_room.w_to
            else:
                print("")
                print("Oops, there's no room there.")

    # If player in Room, if he picks up item, remove item from that ROOM and add it to player's items list.

# emilio = Player("Emilio Ramirez", "Sala")
# print(emilio)
# print(repr(emilio))
