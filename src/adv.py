from room import Room
from player import Player
from colorama import Fore, Style
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p1 = Player("", room['outside'])


def name(confirm="n"):
    valid = {
        "yes": True,
        "y": True,
        "ye": True,
        "no": False,
        "n": False
    }

    while valid[confirm] is False:
        if confirm not in valid:
            print(f"{Fore.RED}Incorrect input: {confirm}, please try again.{Style.RESET_ALL}")   

        p1_name = input("What is your name? ")
        if p1_name != '':
            confirm = input(f"Your name is {Fore.GREEN}{p1_name}{Style.RESET_ALL}, is that correct? ")

    print(f"Welcome to the game, {Fore.GREEN}{p1_name}{Style.RESET_ALL}")
    return p1_name


p1.name = name()


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def game(move=None):
    correct = [
        "N",
        "S",
        "E",
        "W",
        "n",
        "s",
        "e",
        "w",
        "q"
    ]
    print(p1)

    while move is None or move.lower() != "q":
        move = input("Where do you want to go? \n [N] [S] [E] [W] \n To quit the game hit [Q] ")

        if move not in correct:
            print(f"{Fore.RED}Please enter either: [N] [S] [E] [W], or [Q] to quit{Style.RESET_ALL}")
        
        if p1.room is None:
            print(f"You can't go that way, returning you from whence you came...")
            p1.room = room['outside']
            print(p1)

        if move in correct and move == "n" or move == "N":
            new_room = p1.room.n_to
            p1.room = new_room
            print(p1)
        if move in correct and move == "s" or move == "S":
            new_room = p1.room.s_to
            p1.room = new_room
            print(p1)
        if move in correct and move == "e" or move == "E":
            new_room = p1.room.e_to
            p1.room = new_room
            print(p1)
        if move in correct and move == "w" or move == "W":
            new_room = p1.room.w_to
            p1.room = new_room
            print(p1)
    
    return f"Goodbye, {Fore.GREEN}{p1.name}{Style.RESET_ALL}!"
            







print(game())