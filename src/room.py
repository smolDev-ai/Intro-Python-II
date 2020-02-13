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

    def __str__(self):
        desc_string = ""
        desc_string += f"{self.name}: \n{self.desc()}"
        return desc_string

    def desc(self):
        wrapper = textwrap.TextWrapper(width=70)
        desc = wrapper.fill(text=self.description)
        return f"{desc}"

    def show_items(self):
        if len(self.items):
            print(f"{Style.BRIGHT}Items in the room:{Style.RESET_ALL}")
            for i in self.items:
                print(f"{Fore.GREEN}{Style.BRIGHT}{i.name}: {i.description}{Style.RESET_ALL}")
        else:
            return None

    def remove_item(self, item):
        for i in self.items:
            if item == i.name:
                self.items.remove(i)