from colorama import Fore, Style
from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = inventory

    def add_item(self, new_item):
        self.inventory.append(Item(new_item))
        print(f"{self.name} added the {new_item} to their inventory")

    def __str__(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL} is in {Fore.YELLOW}{self.room}{Style.RESET_ALL}"
