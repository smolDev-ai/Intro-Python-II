import textwrap
from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.

wrapper = textwrap.TextWrapper(width=50)


class Room:
    def __init__(self, name, description, items=[], n=None, s=None, e=None, 
                 w=None):
        self.name = name
        self.description = description
        self.n = n
        self.s = s
        self.e = e
        self.w = w
        self.items = items

    description_str = ""

    def desc(self):
        wrapper = textwrap.TextWrapper(width=70)
        desc = wrapper.fill(text=self.description)
        return f"{desc}"

    def show_items(self):
        if len(self.items):
            for i in self.items:
                global description_str f"{i.name}: {i.description}\n"
        else:
            return None

    def __str__(self):
        return f"{self.name}:\n{Room.desc(self)}\nItems here: {description_str}"
