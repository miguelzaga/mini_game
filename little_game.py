from sys import exit

def die(reason):
    print(reason, "Good job!")
    exit(0)

def beginning():
    print("You wake up in a dark room. You barely see a door in front of you")
    x = input("> ")

    if "door" in x or "open" in x:
        print("You open the door")
        print("You walk through a corridor. It's walls are naked bricks")
        corridor()

    else:
        print("I didn't get it")
        beginning()

def corridor():
    print("The corridor divides in two paths. Do you take the left or right?")
    x = input("> ")

    if x == "left":
        sword_room()

    elif x == "right":
        statue_room()

    elif "back" in x:
        beginning()

    else:
        print("I didn't get it")
        corridor()

def sword_room():
    global sword_in_room
    global sword_equipped

    print("You are in a small green room")
    print("There is a red botton with a sign over it")

    if sword_in_room == True:
        print("Besides it there is a sword")

    x = input("> ")

    if "sword" in x:

        if sword_in_room == True:
            sword_in_room = False
            sword_equipped = True
            print("You take the sword")
            sword_room()

        elif sword_in_room == False:
            print("You already have taken the sword")
            sword_room()


    elif "read" in x:
        print("The signs says:")
        print("DO NOT PRESS THE BOTTON")
        sword_room()

    elif "botton" in x:
        print("You press the botton")
        print("A trap door opens beneath your")
        die("You fall on iron spikes and die instantly")

    elif "exit" == x or "return" == x:
        print("You leave the room")
        corridor()
    else:
        print("I didn't get it")
        sword_room()


def statue_room():

    print("You are in a large cold salon")
    print("In the middle of it there is a statue of a warrior")
    print("You notice that its hands are made of ice")

    x = input("> ")

    if "cut" in x and sword_equipped == True:
        print("You cut the statue's hands")
        print("It turns to live and the room get colder")
        die("The statue embraces you and you slowly freeze to death")

    elif "grab" in x or "hand" in x:
        print("You grab the statue's hands and they melt")
        print("A passage opens and fills the room with light")
        print("You go through it and the opening closes behind you")

        forest()

    else:
        print("Nothing happens")

def forest():

    print("---------------------------")
    print("You are in a beatiful forest")
    print("There are two paths in front of you")
    print("One seems to lead to a savannah and the other to a river")

    x = input("> ")

    if "savannah" in x:
        print("You start walking towards the savannah")
        savannah()

    elif "river" in x:
        print("You start walking towards the river")
        river()

    else:
        print("Decide a path man")
        forest()


def savannah():

    print("You see a lion in the distance")
    print("It is running towards you")

    if sword_equipped == True:
            print("You cut it's throat with the sword")
            print("A blondy comes from the bushes and cleans the blood off your face")
            die("Congratulations")
    else:
        print("You have no way to defend yourself")
        die("The lion crushes your skull")

def river():

    print("You see a bear in the distance")
    print("It is running towards you")

    if sword_equipped == True:
            print("You cut it's throat with the sword")
            print("Behind the death bear you notice a chest full of gold")
            die("Congratulations")
    else:
        print("You have no way to defend yourself")
        die("The bear eats you alive")

sword_equipped = False
sword_in_room = True
beginning()
