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
        if items == None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def __repr__(self):
        return f"Room({self.name}, {self.description})"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        if len(self.items):
            for item in self.items:
                print("")
                print("Room has these items:")
                print('-->', item.name)
        else:
            print("")
            print("Room doesn't have any items right now.")
