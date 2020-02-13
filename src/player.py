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
        if len(self.inventory) < 2:
            self.inventory.append(new_item)
            self.room.remove_item(new_item)
            print(f"{Fore.GREEN}{self.name}{Style.RESET_ALL} added the {Fore.BLUE}{new_item.name}{Style.RESET_ALL} to their inventory\n")
            print(f"\n{Style.BRIGHT}Your inventory now contains: {Style.RESET_ALL}")
            for items in self.inventory:
                print(f"{Fore.BLUE}{items.name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}You can't carry any more items right now!{Style.RESET_ALL}")

    def remove_item(self, dropped):
        if len(self.inventory) == 0:
            print(f"{Fore.RED}You don't have any items!{Style.RESET_ALL}")
        else:
            for i in self.inventory:
                if dropped == i.name.lower():
                    self.inventory.remove(i)
                    self.room.add_item(i)
                    print(f"{Fore.GREEN}{self.name}{Style.RESET_ALL} dropped {Fore.BLUE}{dropped}{Style.RESET_ALL}\n")

    def get_inventory(self):
        if len(self.inventory):
            print(f"{Style.BRIGHT}Your inventory contains: {Style.RESET_ALL}")
            for i in self.inventory:
                print(f"{Fore.BLUE}{i}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Your inventory is empty!{Style.RESET_ALL}")
    
    def __str__(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL} is in {Fore.YELLOW}{self.room}{Style.RESET_ALL}"
