from colorama import Fore, Style
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"{Fore.GREEN}{self.name}{Style.RESET_ALL} is in {Fore.YELLOW}{self.room}{Style.RESET_ALL}"
