import sys;
import json;
from collections import namedtuple

filename = sys.argv[1]

with open(filename, 'r') as file:
    data = json.load(file)

user_inventory = [];

help_verbs = {'go': '...', 'get': '...', 'look': '', 'drop': '...', 'inventory': '', 'quit': '', 'help': ''};


def read(ind):
    global map_object
    map_object = data[ind]

    print(map_object['name'])
    print(map_object['desc'])
    print()
    if ('items' in map_object):
        print("Items:", end=" ")
        for item in map_object['items']:
            print(item, end=" ")
        print("\n")
    exits = map_object['exits']
    print("Exits:", end=" ")
    for key in exits:
        print(f'{key}', end=" ");
    print("\n")


def process():
    while (True):

        try:
            instruction = str(input("What would you like to do? "))
            instruction = instruction.lower();
            command = instruction.split(" ");

            # Directions become verb extension
            if (len(command) == 1):
                abbrevation_direction = command[0]

                if (abbrevation_direction == "e"):
                    command[0] = "go"
                    command.insert(1, "east")

                if (abbrevation_direction == "w"):
                    command[0] = "go"
                    command.insert(1, 'west')

                if (abbrevation_direction == "s"):
                    command[0] = "go"
                    command.insert(1, 'south')

                if (abbrevation_direction == "n"):
                    command[0] = "go"
                    command.insert(1, 'north')

                if (abbrevation_direction == "ne"):
                    command[0] = "go"
                    command.insert(1, 'northeast')

                if (abbrevation_direction == "nw"):
                    command[0] = "go"
                    command.insert(1, 'northwest')

                if (abbrevation_direction == "ns"):
                    command[0] = "go"
                    command.insert(1, 'northsouth')

                if (abbrevation_direction == "se"):
                    command[0] = "go"
                    command.insert(1, 'southeast')

                if (abbrevation_direction == "sw"):
                    command[0] = "go"
                    command.insert(1, 'southwest')

        except EOFError as e:
            print(f'Use \'quit\' to exit.')
            continue
        verb = command[0]
        present = False
        item_found = False
        if (verb == "go"):

            if (len(command) < 2):
                print(f'Sorry, you need to \'{verb}\' somewhere.')
                continue
            direction = command[1]
            exits = map_object['exits']
            direction_matched = []
            for key in exits:
                if (key == direction):
                    present = True
                    global value
                    value = exits[key]
                    print(f'You go {direction}.\n')
                    read(value)

                elif (direction in key and present == False):
                    direction_matched.append(key)

            # Abbrevations for Direction feature
            if (len(direction_matched) >= 1):
                print("Did you want to go", end=" ")

                for i in range(0, len(direction_matched) - 1):
                    print(direction_matched[i], end=" or ")
                print(direction_matched[len(direction_matched) - 1] + "?")
                continue

        if (verb == "go" and present == False):
            print(f'There\'s no way to go {direction}.')

        if (verb == "look"):
            read(value)

        if (verb == "get"):

            if (len(command) < 2):
                print(f'Sorry,What do you need to {verb}?')
                continue
            if (hasattr(map_object, 'items')):
                item_to_get = command[1]
                items = map_object['items']
                items_matched = [];
                for item in items:

                    # exact match condition
                    if (item == item_to_get):
                        item_found = True
                        user_inventory.append(item)
                        items.remove(item)
                        print(f'You pick up the {item}.')

                    elif (item_to_get in item):
                        items_matched.append(item)

                if (len(items_matched) == 1):
                    item_found = True
                    user_inventory.append(items_matched[0])
                    items.remove(items_matched[0])
                    print(f'You pick up the {items_matched[0]}.')


                # Items should be matchable based on any included string feature:
                elif (len(items_matched) == 2):
                    item_found = True
                    print(f'Did you want to get the {items_matched[0]} or the {items_matched[1]}?')
                elif (len(items_matched) > 2):
                    item_found = True
                    print("Did you want to get the", end=" ")

                    for i in range(0, len(items_matched) - 1):
                        print(f'{items_matched[i]},', end=" ")
                    print(f'or the {items_matched[len(items_matched) - 1]}?')

                if (item_found == False):
                    print(f'There is no {item_to_get} anywhere.')
            else:
                print(f'There is no {item_to_get} anywhere.')

        if (verb == "inventory"):

            if (len(user_inventory) == 0):
                print("You're not carrying anything.")
            else:
                print("Inventory:")
                for item in user_inventory:
                    print(f' {item}')

        if (verb == "quit"):
            print("Goodbye!")
            break

        # Help extension
        if (verb == "help"):

            for key, value in help_verbs.items():
                print(key, value)

        # Drop extension
        if (verb == "drop"):

            if (len(command) < 2):
                print(f'Sorry,What do you need to {verb}?')
                continue
            if ('items' in map_object):
                item_to_drop = command[1]
                items = map_object['items']
                for item in user_inventory:
                    if (item == item_to_drop):
                        item_found = True
                        items.append(item)
                        user_inventory.remove(item)
                        print(f'You drop  the {item}.')
                if (item_found == False):
                    print(f'There is no {item_to_drop} to drop anywhere.')
            else:

                item_to_drop = command[1]
                map_object['items'] = []
                items = map_object['items']
                for item in user_inventory:
                    if (item == item_to_drop):
                        item_found = True
                        items.append(item)
                        user_inventory.remove(item)
                        print(f'You drop  the {item}.')
                if (item_found == False):
                    print(f'There is no {item_to_drop} to drop anywhere.')


read(0)
process()