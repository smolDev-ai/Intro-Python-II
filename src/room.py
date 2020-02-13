import textwrap
from colorama import Fore, Style
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

    def desc(self):
        wrapper = textwrap.TextWrapper(width=70)
        desc = wrapper.fill(text=self.description)
        return f"{desc}"

    def remove_item(self, item):
        for i in self.items:
            if Item.name == i.name:
                self.items.remove(i)
                print(f"\n\n{Style.BRIGHT}Items in the area:{Style.RESET_ALL} \n{Fore.GREEN}{i.name}: {i.description}{Style.RESET_ALL}")

    def __str__(self):
        return f"{self.name}: \n{Room.desc(self)}"
