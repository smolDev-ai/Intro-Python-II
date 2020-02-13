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
        self.inventory.append(new_item)
        print(f"{Fore.GREEN}{self.name}{Style.RESET_ALL} added the {Fore.BLUE}{new_item.name}{Style.RESET_ALL} to their inventory")
        print(f"Your inventory now contains: ")
        for items in self.inventory:
            print(f"{Fore.BLUE}{items.name}{Style.RESET_ALL}")

    def get_inventory(self):
        if len(self.inventory) > 0:
            print(f"{Style.BRIGHT}Your inventory contains: {Style.RESET_ALL}")
            for i in self.inventory:
                print(f"{Fore.BLUE}{i}{Style.RESET_ALL}")
        else:
            print("Your inventory is empty!")
    
    def __str__(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL} is in {Fore.YELLOW}{self.room}{Style.RESET_ALL}"
