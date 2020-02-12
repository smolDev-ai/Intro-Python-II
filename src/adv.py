from room import Room
from player import Player
from colorama import Fore, Style
from item import Item
# Declare all the rooms

item1 = Item("Sword", "This is a sword.")
item2 = Item("Wand", "This is a wand.")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item1, item2]),

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

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

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

def game(command=None):
    moves = [
        "n",
        "s",
        "e",
        "w",
    ]

    other_commands = [
        "h",
        "where",
        "whereami",
        "q"
    ]
    print(p1)

    while command is None or command != "q":
        command = input("Where do you want to go? ").strip().lower()

        if command not in moves and command not in other_commands:
            print(f"{Fore.RED}Incorrect Input, press [H] for help!{Style.RESET_ALL}")

        room = getattr(p1.room, command, None)

        if command in moves and room != None:
            p1.room = room
            print(p1)

        elif command in other_commands:
            if command == "where" or command == "whereami":
                print(p1)

            if command == "h":
                print(f"\n{Fore.BLUE}[N]{Style.RESET_ALL} -> Moves the character North.\n"
                      f"{Fore.BLUE}[S]{Style.RESET_ALL} -> Moves the character South.\n"
                      f"{Fore.BLUE}[E]{Style.RESET_ALL} -> Moves the character East.\n"
                      f"{Fore.BLUE}[W]{Style.RESET_ALL} -> Moves the character West.\n"
                      f"{Fore.MAGENTA}[take \"item\"]{Style.RESET_ALL} -> picks up the specified item.\n"
                      f"{Fore.MAGENTA}[drop \"item\"]{Style.RESET_ALL} -> drops the specified item.\n"
                      f"{Fore.MAGENTA}[where/whereami]{Style.RESET_ALL} -> Gives character's current location.\n"
                      f"{Fore.RED}[Q]{Style.RESET_ALL} -> quits the game.\n\n")
        else:
            print(f"{Fore.RED} You can't go that way...{Style.RESET_ALL}")
            print(p1)
    
    return f"Goodbye, {Fore.GREEN}{p1.name}{Style.RESET_ALL}!"
            

# Notes To Myself:
# When you create your items tomorrow, make an items class and aggregate it
# onto the player and room classes
# rooms can have any number of items
# Limit the number of items a player can hold to two (items[:3] to start)
# when a player picks up and item, remove it from the items within the room,
# and add it to the player list.
# implement a call that lets the player know that they have reached their
# given limit of items
# if the player tries to pick up another item after their list has been filled,
# have them drop one.
# Do not allow them to move on, until they do.

print(game())
