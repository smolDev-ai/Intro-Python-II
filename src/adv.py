from room import Room
from player import Player
from colorama import Fore, Style
from item import Item
# Declare all the rooms



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",),

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


# add items to rooms:
items = {
    "Sword": Item("Sword", "This is a sword."),
    "Wand": Item("Wand", "This is a wand."),
    "Spear": Item("Spear", "This is a spear."),
    "Rope": Item("Rope", "This is a long rope."),
    "Harp": Item("Harp", "Once a beautiful instrument, now it's strings are broken."),
    "Flute": Item("Flute", "A flute.")

}

# add items to rooms:
room['outside'].items = [
    items['Wand'],
    items['Sword'],
    items['Spear']
]
room['foyer'].items = [
    items['Rope'],
    items['Harp']
]

room['narrow'].items = [
    items['Flute']
]

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
        "help",
        "where",
        "whereami",
        "q",
        "i",
        "bag",
        "take",
        "get",
        "drop"
    ]
    print(p1)
    p1.room.show_items()

    while command is None or command[0] != "q":
        command = input("\nWhat do you want to do? ").strip().lower().split(' ')
        main_command = command[0]

        if main_command not in moves and main_command not in other_commands:
            print(f"{Fore.RED}Incorrect Input, press [H] for help!{Style.RESET_ALL}")

        movement = f"{main_command}_to"
        room = getattr(p1.room, movement, None)

        if main_command in moves and room is not None:
            p1.room = room
            print(p1)
            p1.room.show_items()

        elif main_command in other_commands:
            if main_command == "where" or main_command == "whereami":
                print(p1)
                p1.room.show_items()

            if main_command == "take" or main_command == "get":
                item = command[1]
                p1.add_item(items[item.title()])
                p1.room.show_items()

            if main_command == "drop":
                item = command[1]
                p1.remove_item(item)
                
                p1.room.show_items()

            if main_command == "i" or main_command == "bag":
                p1.get_inventory()

            if main_command == "h" or main_command == "help":
                print(f"\n{Fore.BLUE}[N]{Style.RESET_ALL} -> Moves the character North.\n"
                      f"{Fore.BLUE}[S]{Style.RESET_ALL} -> Moves the character South.\n"
                      f"{Fore.BLUE}[E]{Style.RESET_ALL} -> Moves the character East.\n"
                      f"{Fore.BLUE}[W]{Style.RESET_ALL} -> Moves the character West.\n"
                      f"{Fore.MAGENTA}[take/get \"item\"]{Style.RESET_ALL} -> picks up the specified item.\n"
                      f"{Fore.MAGENTA}[drop \"item\"]{Style.RESET_ALL} -> drops the specified item.\n"
                      f"{Fore.MAGENTA}[i/bag]{Style.RESET_ALL} -> Shows items in character's inventory.\n"
                      f"{Fore.MAGENTA}[where/whereami]{Style.RESET_ALL} -> Gives character's current location.\n"
                      f"{Fore.RED}[Q]{Style.RESET_ALL} -> quits the game.\n\n")
        else:
            print(f"{Fore.RED} You can't go that way...{Style.RESET_ALL}")
            print(p1)
    
    return f"Goodbye, {Fore.GREEN}{p1.name}{Style.RESET_ALL}!"


print(game())
