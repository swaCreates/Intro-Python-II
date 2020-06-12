from room import Room
from player import Player

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

choice = ['n', 's', 'e', 'w', 'q']

# Make a new player object that is currently in the 'outside' room.

while True:
    print('press [q] to quit the game')
    name = input('Enter a name for your character: ' )
    if name == '':
        break
    if name == 'q':
        break
    else:
        current_room = room['outside']
        player_1 = Player(name, current_room)
        print(player_1)
        break

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

while True:
    if name == '':
        print(f'Please provide character name')
        break
    elif name == 'q':
        print('You have quit the game')
        break
     
    print('press [q] to quit the game')
    choice = input(f'{player_1.name} choose your narrow path wisely: [n] [s] [e] [w]  ').lower()
    no_room_err= 'The room you have chosen has been cloaked. We cannot find it!'

    if choice == 'q':
        print('You have quit the game, thank you for playing :)')
        break
    if choice == 'n':
        #  we want to test our current room against the room we are trying to go to, and see if we can move there

        if player_1.current_room == room['outside']: # could also remove is not None
            player_1.current_room= room['foyer']
            print(player_1.current_room)
        elif player_1.current_room == room['foyer']: 
            player_1.current_room= room['overlook']
            print(player_1.current_room)
        elif player_1.current_room == room['narrow']:
            player_1.current_room= room['treasure']
            print(player_1.current_room)
        else:
            print(no_room_err)
    elif choice == 's':
        if player_1.current_room == room['foyer']:
            player_1.current_room= room['outside']
            print(player_1.current_room)
        elif player_1.current_room == room['overlook']:
            player_1.current_room= room['foyer']
            print(player_1.current_room)
        elif player_1.current_room == room['treasure']:
            player_1.current_room= room['narrow']
            print(player_1.current_room)
        else:
            print(no_room_err)
    elif choice == 'e':
        if player_1.current_room == room['foyer']:
            player_1.current_room= room['narrow']
            print(player_1.current_room)
        else:
            print(no_room_err)
    elif choice == 'w':
        if player_1.current_room == room['narrow']:
            player_1.current_room= room['foyer']
            print(player_1.current_room)
        else:
            print(no_room_err)
    else:
        print('You cannot waiver to this path! Choose again!')
   
