

room = ['Entrance Hall','Library','Kitchen','Garden']
commands = ['N','S','E','W','quit','help']
description = [
    "A grand foyer with a crystal chandelier",
    "Dusty bookshelves stretch from floor to ceiling",
    "Copper pots hang above an old stone hearth",
    "Overgrown vines twist around marble statues"
]
current = 0
gameover = False

print("You are in the: "+room[current])
print(description[current])


while gameover == False: 
    command = input("Enter command: ")
    while command not in commands:
        print("Error! Not a valid command.")
        command = input("Enter command: ")

    temppos = current
    validmove = False
    if command == "N":
        current -= 2
        validmove = True
    elif command == "S":
        current += 2
        validmove = True
    elif command == "E" and (current != 3 and current != 1):
        current += 1
        validmove = True
    elif command == "W" and current != 2:
        current -= 1
        validmove = True
    elif command == "quit":
        gameover = True
        validmove = True
    elif command == "help":
        print("Commands available are: N, S, E, W, help, quit\n")
        validmove = True

    if not validmove:
        print("You can't move in that direction")
        print()
        current = temppos

    

    print("You are in the: "+room[current])
    print(description[current])