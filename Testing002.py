bedroom = {"look out window":"You slowly stride towards the window. You reach forward and push aside the curtains," + 
           " squinting against the harsh light of the sun. It sits above the horizon, ready to encase the suburban neighborhood in darkness." +
           " Many replicas of your house adorn the streets, but there's nothing important to note.\n\n",
           
           "look in closet":"You move to the closet, opening the doors. It's bare of any clothes; the bottom of the closet is empty," +
           " but there remains only one jacket in a hanger.\n\n",
           
           "head out the room":"You move to the door with dragging feet, opening the door and revealing the hallway.\n\n" +
           "Your bedroom is the last door at the end of this hallway, revealing two more doors, one on the right and one on the left, before the hall reveals" +
           " the living room. The wallpaper is yellowed and peeling, bare of any decorations. Stains of unknown origin are all that greets you, colored in a washed," +
           " deep red and what looks like soot."}

closet = {"take the jacket":"You pick up the jacket and discard the hanger, pulling it over your arms and shrugging it over your shoulders." +
          " The jacket is worn but comfortable, calming you down from the lingering anxiety of my nightmare.\n\n"}

jacket = {"search the jacket":"In the jacket pockets, you find a pack of untouched cigarettes.\n\n"}

hallway = {"right":"You walk to the door on the right, and upon opening the door, you reveal a small bathroom with a single sink, toilet, and a bathtub and shower" +
           " combination. Stepping into the bathroom, you look in the mirror.\n\nYou look tired with dark bruises underneath your eyes. Turning the faucet on, the" +
           " water pressure is minimal yet still clean-looking, and you pool water in your cupped hands, splashing it against your face.\n\n",
           
           "left":"You move to the door on the left, revealing a small office. There's one window with the burned remains of a curtain barely hanging to the mantle." +
           " It only blocks the top of the window with scraps creating a silhouette in the barren office. A desk made of what once was wood is simply charcoal, standing" +
           " on a husk of itself. The stench of the office is enough to make your eyes water and your nose burn.\n\n",
           
           "enter the living room":"You travel down the hall into the living room, surveying how you left the state of the place. There isn't anything you remember leaving" +
           " behind.\n\n" +
           "\tYOU: Damn, guess I forgot to clean up. It's messy around here.\n\n" +
           "The couch is covered in soot, and the windows are all bare of their curtains. The walls are blackened with a substance.\n\n" +
           "\tYOU: I could never get those stains to come out... Dunno what it is.\n\n" +
           "Adorning the walls are burned picture frames whose contents are blurred or burned or smudged away.\n\n" +
           "\tYOU: Could never remember what they were.\n\n" +
           "Beside the couch is the door that leads to the backyard with a glass sliding door, revealing a treeline that seemingly features an endless sea of trees." +
           " There is another archway that leads into the kitchen."}

bathroom = {"search the bathroom":"The only thing you can find are ashes littered amongst the countertop of the sink and the small, lone window just above the toilet." +
           " There is nothing else left to note.\n\n"}

office = {"search the office":"You take a few steps towards the desks and notice a few picture frames. Its contents are burned just like its living area, but you notice" +
          " that there's only one frame that holds a piece of a picture that's burned at the edges.\n\n"}

office_burnedpic = {"take the piece of burned picture":"You carefully peel away the edges of the picture frame and manage to pick up the remaining burned piece of the picture. It" +
                    " seems to have split into one corner of the rectangular picture. The picture is of the bottom left part of the frame, showing the legs of two children and two" +
                    " adults.\n\n"}

living_room = {"go to kitchen":"The kitchen is bare like the rest of the house with only an empty sink, an empty fridge, and empty walls to greet you. Connected to the" +
               " kitchen is the front door.\n\n",
               
               "go to backyard":"You decide to head outside, cringing a bit at the whining noise of the sliding back door. You step into your shoes and walk towards the" +
               " treeline where there seems to be dense woods bordering the edge of the backyard. It's full and darkens a few mere feet into the treeline. You feel uneasy" +
               " staring into the woods and don't wish to step any further.\n\n" +
               "You turn around to head back into the house, but you stop to view it. For a moment, you smell smoke burning your nostrils, making you sneeze. When you look" +
               " up again, the house seems to be in okay condition. It feels like nothing is out of sorts.\n\n" +
               "\tYOU: I wonder what that was...\n\n" +
               "You head back inside the living room.\n\n"}

kitchen = {"search the kitchen":"The kitchen has bags full of trash littering the floor and mounds of ash cover the window sills and sink. It strangely doesn't smell" +
           " like anything.\n\n" +
           "\tYOU: Wonder if my sense of smell finally got snuffed out.\n\n" +
           "The dining table is directly connected to the kitchen. You notice that it has a broken piece of glass where a picture frame sits.\n\n",
           
           "head outside and into town":"You head to the front door, grab your keys hanging on the key holder beside it, and go outside. You survey the small" +
           " suburban neighborhood where replicas of your own house are repeated throughout the whole street.\n\n" +
           "\tYOU: Weird. There's usually kids screaming outside at this hour.\n\n" +
           "The whole neighborhood is quiet, and it makes you feel on edge, like something is wrong, yet you can't put your finger on it. You shake the feeling off" +
           " as best as you can and head to your SUV, deciding to drive downtown.\n\n"}


def getActions(location):
    for key in location.keys():
        print("- ", key)


inventory = []

running = True

# Main game loop
while running:
    print("You are, and forever will be, unfinished...\n\n")
    print("You wake up from a nightmare, sitting straight up in your bed. Your skin is slicked with sweat, and your heart pounds in your chest.\n\n")
    print("You can't recall the specific details of the nightmare.\n\n")
    print("\tYOU: It was just a nightmare...\n\n")
    print("The bed is pushed to the center of the back wall. There's a window to your right covered by curtains, and the door remains closed to your far left." +
        " Just beside the door are the closet doors that also remain shut. There's nothing else in the room for you to note.\n\n")
    
    # Starting at bedroom, display all actions one can take
    getActions(bedroom)
    action = input("\n\n> ")

    for key in bedroom.keys():
        if action == key:
            print("\n", bedroom[key])

            # Special case; needs to account for spaces in spaces
            if action == "look in closet":
                getActions(closet)
                action = input("\n> ")
                if action == "take the jacket":
                    print("\n", closet["take the jacket"])
                    print("Jacket has been added to your inventory.\n")
                    inventory.append("jacket")
                    getActions(jacket)
                    action = input("\n> ")
                    if action == "search the jacket":
                        print("\n", jacket["search the jacket"])
                        getActions(bedroom)
            elif action == "head out the room":
                break

            action = input("> ")

    # Now in hallway
    getActions(hallway)
    action = input("\n\n> ")

    for key in hallway.keys():
        if action == key:
            print("\n", hallway[key])

            # Special cases
            if action == "right":
                getActions(bathroom)
                action = input("\n> ")
                if action == "search the bathroom":
                    print("\n", bathroom["search the bathroom"])
                    getActions(hallway)
            elif action == "left":
                getActions(office)
                action = input("\n> ")
                if action == "search the office":
                    print("\n", office["search the office"])
                    getActions(office_burnedpic)
                    action = input("\n> ")
                    if action == "take the piece of burned picture":
                        print("\n", office_burnedpic["take the piece of burned picture"])
                        print("1/3 piece of burned picture added to inventory.\n")
                        inventory.append("1/3 piece of burned picture")
                        getActions(hallway)
            elif action == "enter the living room":
                break

            action = input("\n> ")
    
    # Now in the living room
    getActions(living_room)
    action = input("\n\n> ")

    for key in living_room.keys():
        if action == key:
            print("\n", living_room[key])

            # Special cases
            if action == "go to kitchen":
                getActions(kitchen)
                action = input("\n\n> ")
                if action == "search the kitchen":
                    print("\n", kitchen["search the kitchen"])
                    getActions(kitchen)
                    action = input("\n\n> ")
                elif action == "head outside and into town":
                    print("\n", kitchen["head outside and into town"])
                    break

    running = False

