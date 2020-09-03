# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        # Room should have some items to start with.
        if items == None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def __repr__(self):
        return f"Room({self.name}, {self.description})"


# room = Room("Levofit", "Sala para hacer crossfit")
# print(room)
# print(repr(room))
