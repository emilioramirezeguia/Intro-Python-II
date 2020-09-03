# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def __repr__(self):
        return f"Room({self.name}, {self.description})"


# room = Room("Levofit", "Sala para hacer crossfit")
# print(room)
# print(repr(room))
