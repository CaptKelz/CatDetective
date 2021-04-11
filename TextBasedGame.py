# Kelly Nachazel

# dictionary of rooms with items and directions
room_items = {
    "Park Entrance": {
        "north": "The Soccer Field",
        "west": "The Skatepark",
        "east": "The Campsite",
        "item": "Start"
    },
    "The Skatepark": {
        "north": "The Soccer Field",
        "east": "Park Entrance",
        "item": "Leaf the Green Kitten"
    },
    "The Campsite": {
        "north": "The Pond",
        "west": ["The Soccer Field", "Park Entrance"],
        "item": "Fire the Red Kitten"
    },
    "The Soccer Field": {
        "north": ["The Forest", "The Playground"],
        "east": "The Campsite",
        "south": ["The Skatepark", "Park Entrance"],
        "item": "Flower the Orange Kitten"
    },
    "The Playground": {
        "west": "The Forest",
        "south": "The Soccer Field",
        "east": "The Pond",
        "item": "Bebe the Grey Kitten"
    },
    "The Pond": {
        "west": "The Playground",
        "south": "The Campsite",
        "item": "Catnapper"
    },
    "The Forest": {
        "north": "The Cave",
        "south": "The Soccer Field",
        "west": "The Playground",
        "item": "Rainbow the Pink Kitten"
    },
    "The Cave": {
        "south": "The Forest",
        "east": "The Playground",
        "item": "Midnight the Black Kitten"
    },
}
# initialize game variables
move_commands = ("go north", "go south", "go east", "go west")
game_status = "continue"
current_room = "Park Entrance"
inventory = []
user_command = ""
item = "Start"

# check for a room in given direction
def move_rooms(command):
    command.lower()
    direction = command.split(" ")
    move = direction[1]
    temp_dict = room_items[current_room]
    if move in temp_dict.keys():  # checks dictionary for a room in the given direction
        # exception with 2 rooms in the same direction
        if current_room == 'The Soccer Field' or current_room == 'The Campsite':
            if type(room_items[current_room][move]) is list:
                print('Do you want to go to [1] {} or [2]{}?'.format(room_items[current_room][move][0],
                                                                     room_items[current_room][move][1]))
                print('Enter the number of your choice.')
                choice = int(input())
                while choice < 1 or choice > 2:
                    print('That is not a valid choice.')
                    choice = int(input())
                room = room_items[current_room][move][choice - 1]
                return room
            else:
                room = room_items[current_room][move]
                return room
        else:
            room = room_items[current_room][move]
            return room
    else:
        room = current_room
        print("There is no room in that direction!")
        return room


# game dialogue and command prompt
def game_prompt(room):
    print()
    print("You are at {}".format(room))
    print("Inventory: {}".format(inventory))


# add kitten to inventory
def add_kitten(room, command):
    command_key = command.split(' ')
    room_kitten = room_items[room]['item'].split(' ')
    while command_key[1] != room_kitten[0]:
        print('This cat is not here. Try again!')
        command = input()
        command_key = command.split(' ')
    kitten = room_items[room]['item']
    return kitten


# check if the game is won or lost
def get_game_status(room):
    if room_items[room]['item'] == 'Catnapper':
        status = 'exit'
    elif len(inventory) == 6:
        status = 'winner'
    else:
        status = 'continue'
    return status


# Introduction and beginning instructions
print("The Cat Detective Game\n"
      "\n"
      "Find all 6 kittens before the Catnapper to win the game!\n"
      "Move commands: go north, go south, go east, go west\n"
      "Collect the kitten: catch 'kitten name'\n"
      "----------------------------------------")
game_prompt(current_room)
user_command = input("What is your move?: ")
while game_status == 'continue':
    if user_command in move_commands:
        current_room = move_rooms(user_command)
        game_status = get_game_status(current_room)
        game_prompt(current_room)
        item = room_items[current_room]['item']
        if item != 'Start' and item not in inventory:
            print('You found {}!'.format(item))
        user_command = input("What is your move?: ")
    elif user_command[0:5] == 'catch':
        if item not in inventory:
            inventory.append(add_kitten(current_room, user_command))
        game_status = get_game_status(current_room)
        game_prompt(current_room)
        user_command = input("What is your move?: ")
    else:
        print("That is not a valid command.")
        user_command = input("What is your move?")

# end of game
if game_status == "exit":
    print()
    print('You found the Catnapper! Game over!')
else:
    print("You have rescued all the kittens! You win!")
