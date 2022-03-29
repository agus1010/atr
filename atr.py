from sys import argv

def boards():
    print("all boards")

def board():
    print("board name")

def error():
    print("hubo un error")

def showhelp():
    print("THIS IS HELP. IS IT HELPING\n")

if len(argv) < 2:
    showhelp()
    exit(2)


switch_program = {
    "boards": boards,
    "board": board,
    "help": showhelp,
}

switch_program.get(argv[1].lower(), error)()
exit(1)