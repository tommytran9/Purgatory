rooms = [
    {
        # Beginning room, ACT 1: SCENE 1
        "description":"You wake up from a nightmare, sitting straight up in your bed. Your skin is slicked with sweat, and your heart pounds in your chest.\n\n" +
        "You can't recall the specific details of the nightmare.\n\n" +
        "\tYOU: It was just a nightmare...\n\n" +
        "The bed is pushed to the center of the back wall. There's a window to your right covered by curtains, and the door remains closed to your far left." +
        " Just beside the door are the closet doors that also remain shut. There's nothing else in the room for you to note.\n\n",

        "actions":["Look out the window", "Look in the closet", "Head out the room"]
     },
     {
         # Look out the window
         "description":"You slowly stride towards the window. You reach forward and push aside the curtains," + 
         " squinting against the harsh light of the sun. It sits above the horizon, ready to encase the suburban neighborhood in darkness." +
         " Many replicas of your house adorn the streets, but there's nothing important to note.\n\n",

         "actions":["Look in the closet", "Head out the room"]
     },
     {
         # Look in the closet
         "description":"You move to the closet, opening the doors. It's bare of any clothes; the bottom of the closet is empty," +
         " but there remains only one jacket in a hanger.\n\n",

         "actions":["Take the jacket", "Look out the window", "Head out the room"]
     },
     {
         # Take the jacket
         "description":"You pick up the jacket and discard the hanger, pulling it over your arms and shrugging it over your shoulders." +
         " The jacket is worn but comfortable, calming you down from the lingering anxiety of my nightmare.\n\n",

         "actions":["Search the jacket", "Look out the window", "Head out the room"]
     },
     {
         # Search the jacket
         "description":"In the jacket pockets, you find a pack of untouched cigarettes.\n\n",

         "actions":["Look out the window", "Head out the room"]
     },
     {
         # Head out the room
         "description":"You move to the door with dragging feet, opening the door and revealing the hallway.\n\n" +
         "Your bedroom is the last door at the end of this hallway, revealing two more doors, one on the right and one on the left, before the hall reveals" +
         " the living room. The wallpaper is yellowed and peeling, bare of any decorations. Stains of unknown origin are all that greets you, colored in a washed," +
         " deep red and what looks like soot.",

         "actions":["Open the door on the right", "Open the door on the left", "Enter the living room", "Go back to the room"]
     },
     {
         # Door on the right
         "description":"You walk to the door on the right, and upon opening the door, you reveal a small bathroom with a single sink, toilet, and a bathtub and shower" +
         " combination. Stepping into the bathroom, you look in the mirror.\n\nYou look tired with dark bruises underneath your eyes. Turning the faucet on, the" +
         " water pressure is minimal yet still clean-looking, and you pool water in your cupped hands, splashing it against your face.\n\n",

         "actions":["Search the bathroom", "Go back to the hallway"]
     },
     {
         # Search the bathroom
         "description":"The only thing you can find are ashes littered amongst the countertop of the sink and the small, lone window just above the toilet." +
         " There is nothing else left to note.\n\n",

         "actions":["Go back to the hallway"]
     },
     {
         # Door on the left
         "description":"You move to the door on the left, revealing a small office. There's one window with the burned remains of a curtain barely hanging to the mantle." +
         " It only blocks the top of the window with scraps creating a silhouette in the barren office. A desk made of what once was wood is simply charcoal, standing" +
         " on a husk of itself. The stench of the office is enough to make your eyes water and your nose burn.\n\n",

         "actions":["Search the office", "Go back to the hallway"]
     },
     {
         # Search the office, take the piece of burned picture?
         "description":"You take a few steps towards the desks and notice a few picture frames. Its contents are burned just like its living area, but you notice" +
         " that there's only one frame that holds a piece of a picture that's burned at the edges.\n\n" +
         "Do you take the piece of burned picture?\n\n",

         "actions":["Yes", "No"]
     },
     {
         # Yes, take the piece of burned picture?
         "description":"You carefully peel away the edges of the picture frame and manage to pick up the remaining burned piece of the picture. It" +
         " seems to have split into one corner of the rectangular picture. The picture is of the bottom left part of the frame, showing the legs of two children and two" +
         " adults.\n\n",

         "actions":["Go back to the hallway"]
     },
     {
         # No, take the piece of burned picture?
         "description":"You leave the burned picture alone, deciding it isn't worth your curiosity.\n\n",

         "actions":["Go back to the hallway"]
     },
     {
         # Enter the living room
         "description":"You travel down the hall into the living room, surveying how you left the state of the place. There isn't anything you remember leaving behind.\n\n" +
         "\tYOU: Damn, guess I forgot to clean up. It's messy around here.\n\n" +
         "The couch is covered in soot, and the windows are all bare of their curtains. The walls are blackened with a substance.\n\n" +
         "\tYOU: I could never get those stains to come out... Dunno what it is.\n\n" +
         "Adorning the walls are burned picture frames whose contents are blurred or burned or smudged away.\n\n" +
         "\tYOU: Could never remember what they were.\n\n" +
         "Beside the couch is the door that leads to the backyard with a glass sliding door, revealing a treeline that seemingly features an endless sea of trees." +
         " There is another archway that leads into the kitchen.",

         "actions":["Go to the kitchen", "Go to the backyard", "Go back to the hallway"]
     },
     {
         # Go to the kitchen
         "description":"The kitchen is bare like the rest of the house with only an empty sink, an empty fridge, and empty walls to greet you. Connected to the" +
         " kitchen is the front door.\n\n",

         "actions":["Search the kitchen", "Head outside and into town", "Go back to the living room"]
     },
     {
         # Search the kitchen
         "description":"The kitchen has bags full of trash littering the floor and mounds of ash cover the window sills and sink. It strangely doesn't smell" +
         " like anything.\n\n" +
         "\tYOU: Wonder if my sense of smell finally got snuffed out.\n\n" +
         "The dining table is directly connected to the kitchen. You notice that it has a broken piece of glass where a picture frame sits.\n\n",

         "actions":["Head outside and into town", "Go back to the living room"]
     },
     {
         # Go to the backyard
         "description":"You decide to head outside, cringing a bit at the whining noise of the sliding back door. You step into your shoes and walk towards the" +
         " treeline where there seems to be dense woods bordering the edge of the backyard. It's full and darkens a few mere feet into the treeline. You feel uneasy" +
         " staring into the woods and don't wish to step any further.\n\n" +
         "You turn around to head back into the house, but you stop to view it. For a moment, you smell smoke burning your nostrils, making you sneeze. When you look" +
         " up again, the house seems to be in okay condition. It feels like nothing is out of sorts.\n\n" +
         "\tYOU: I wonder what that was...\n\n",
         
         "actions":["Go back to the living room"]
     },
     {
         # Head outside and into town
         "description":"You head to the front door, grab your keys hanging on the key holder beside it, and go outside. You survey the small" +
         " suburban neighborhood where replicas of your own house are repeated throughout the whole street.\n\n" +
         "\tYOU: Weird. There's usually kids screaming outside at this hour.\n\n" +
         "The whole neighborhood is quiet, and it makes you feel on edge, like something is wrong, yet you can't put your finger on it. You shake the feeling off" +
         " as best as you can and head to your SUV, deciding to drive downtown.\n\n",

         "actions":["Explore the town", "Go to the church"]
     },
     {
         # Explore the town
         "description":"You park your car and look through the windows of the shops, noticing how none of them are open or accessible. Eventually, you find an" +
         " old newspaper clipping on a nearby table. The newspaper article talks about one of the houses in your neighborhood burning down.\n\n" +
         "Pick up the newspaper article?\n\n",

         "actions":["Yes", "No"]
     },
     {
         # Yes, pick up the newspaper article?
         "description":"You decide to take the newspaper clipping, stuffing it in your pocket. It resonates with you deeply somehow, and you wonder if the residents" +
         " of the house are okay.\n\n",

         "actions":["Go back to the town square"]
     },
     {
         # No, pick up the newspaper article?
         "description":"You don't give the newspaper clipping another thought, turning away.\n\n",
         
         "actions":["Go back to the town square"]
     },
     {
         # Go to the church
         "description":"You then come upon the church with its lights on, and on the porch, you spot a woman in a wedding dress whose face is obscured by Her veil." +
         " She seems to have pale skin underneath Her white dress, and no matter what angle you perceive Her in, you cannot see Her face.\n\n" +
         "\tYOU: Hey there, miss... Are they... holding a wedding today?\n\n" +
         "\tHER: Hello...\n\n" +
         "She says your name, much to your surprise.\n\n" +
         "\tYOU: How do you know my name?\n\n" +
         "You don't recognize Her.\n\n" +
         "\tHER: You simply seem like one...\n\n" +
         "\tHER: No, there's no wedding today.\n\n" +
         "\tYOU: What's with the dress then? If you don't mind me asking.\n\n" +
         "She softly chuckles.\n\n" +
         "\tHER: It's simply a fashion choice. How have you been lately?" +
         "You don't notice the subject change.\n\n" +
         "\tYOU: I... Well, to be honest, I've been pretty tired lately. I don't know why though.\n\n" +
         "\tHER: Is it something personal? Or more of a workplace thing?\n\n" +
         "You feel like this woman is familiar, someone to be trusted. Her voice is soft and soothing, and you find conversing with Her easy.\n\n" +
         "\tYOU: I think it might be more of a personal thing.\n\n" +
         "\tHER: I see… Have you thought about finding solace in your community?\n\n" +
         "You look at the church with a skeptical expression. You purse your lips and try to remain as cordial as possible.\n\n" +
         "\tYOU: If you mean religion, I'm afraid I'm not very religious. I don't… I don't really believe in God, ma'am.\n\n" +
         "She laughs, though it doesn't seem like She moves much at all.\n\n" +
         "\tHER: That's fine...\n\n" +
         "She says your name again, and you feel more comfortable around Her.\n\n" +
         "\tHER: Humor me a little... Join me in the church?\n\n",

         "actions":["Yes", "No"]
     },
     {
         # Yes, go to the church
         "description":"You decide to humor Her and help Her up from Her seat, guiding them into the church. The interior of the church is simple and homely," +
         " a sight that you haven't seen much of at all. It's built of wood and beams with benches laying before the altar where you suppose a priest or" +
         " father would be holding a sermon.\n\n" +
         "You sit with the woman on one of the benches in the middle of the floor.\n\n" +
         "\tHER: What about your personal life has you so weighed down?\n\n" +
         "You take a moment to think about your answer.\n\n"

         # No actions needed, IF HAVE ITEMS or IF NOT HAVE ITEMS
     },
     {
         # No, don't go to the church
         "description":"Even if you feel safe and comfortable around Her, you decide against it. You don't like it when people push you to do things you don't want" +
         " to do.\n\n" +
         "\tYOU: On second thought... I'm sorry, ma'am, but I'm not very comfortable with that.\n\n" +
         "For a moment, you see something underneath the veil that makes the air tense and uncomfortable. Flashes of something horrible come to mind, and your" +
         " stomach sinks; a feeling of dread washes over you, and you take numerous steps back from Her. Belatedly, you realize, it's because of Her.\n\n" +
         "\tHER: Well then... That's a decision I didn't think you'd take.\n\n" +
         "Her voice is dangerously low, and you feel the need to scream.\n\n" +
         "You don't get the chance to.\n\n" +
         "Everything goes black."

         # No actions needed, END OF GAME
     },
     {
         # If you have the items
         "description":"\tYOU: I… I feel like I'm missing something. It hurts here.\n\n" +
         "You pat your chest right above where your heart lays. It makes you sad and uncomfortable that you don't know the reason why you feel so tired.\n\n" +
         "You then look up at Her and have a vague feeling She's giving you a knowing look despite being unable to see Her face.\n\n" +
         "\tHER: Perhaps you are here for something a bit deeper.\n\n" +
         "You give Her a confused look.\n\n" +
         "\tYOU: What do you mean?\n\n" +
         "\tHER: Perhaps you are looking for redemption.\n\n" +
         "You go silent again as you contemplate what She means. As you speak, you sound a bit hesitant, a bit scared.\n\n" +
         "\tYOU: Why… Why would I be looking for redemption?\n\n" +
         "\tHER: Perhaps this church cannot offer what you currently seek.\n\n" +
         "It makes sense to you that you are searching for something, yet you do not know what.\n\n" +
         "\tHER: Visit the red chapel in the black woods. Perhaps you can seek redemption there. Be wary. Don't wander away from the trail; you will get lost." +
         " There are things in those woods that you don't want to see. Be careful.\n\n" +
         "She says this in a soft tone that it was almost mesmerizing for you to hear.\n\n" +
         "\tYOU: Will I see you at this red chapel?\n\n" +
         "\tHER: Perhaps...\n\n" +
         "\tYOU: I'll get to it then.\n\n"

         # No actions needed, NEXT ACT
     },
     {
         # If you don't have the items
         "description":"\tYOU: I… I don't know. I can't say, it's… it's not coming to me.\n\n" +
         "You frown and lean back into the bench a little, searching desperately in your head for a possible reason. You then look back at the woman and have" +
         " the vague feeling that She's frowning at you despite being unable to see Her face.\n\n" +
         "\tHER: Perhaps… you are here for something deeper.\n\n" +
         "Her voice is a little darker, surprising you.\n\n" +
         "\tYOU: What do you mean?\n\n" +
         "\tHER, RESOLUTELY: Perhaps you are looking for redemption.\n\n" +
         "This doesn't make sense to you.\n\n" +
         "\tHER: Visit the red chapel in the black woods. Perhaps you can seek redemption there. Don't wander away from the trail; you will get lost. There are" +
         " things in those woods that you don't want to see.\n\n" +
         "Despite Her earlier tone, it is now soft and mesmerizing for you to hear.\n\n" +
         "\tYOU: Will I see you at this red chapel?\n\n" +
         "\tHER: Perhaps...\n\n" +
         "\tYOU: I'll get to it then.\n\n"

         # No actions needed, NEXT ACT
     },
     {
         
     }
]

church_have_items = {
     "have":"\tYOU: I… I feel like I'm missing something. It hurts here.\n\n" +
     "You pat your chest right above where your heart lays. It makes you sad and uncomfortable that you don't know the reason why you feel so tired.\n\n" +
     "You then look up at Her and have a vague feeling She's giving you a knowing look despite being unable to see Her face.\n\n" +
     "\tHER: Perhaps you are here for something a bit deeper.\n\n" +
     "You give Her a confused look.\n\n" +
     "\tYOU: What do you mean?\n\n" +
     "\tHER: Perhaps you are looking for redemption.\n\n" +
     "You go silent again as you contemplate what She means. As you speak, you sound a bit hesitant, a bit scared.\n\n" +
     "\tYOU: Why… Why would I be looking for redemption?\n\n" +
     "\tHER: Perhaps this church cannot offer what you currently seek.\n\n" +
     "It makes sense to you that you are searching for something, yet you do not know what.\n\n" +
     "\tHER: Visit the red chapel in the black woods. Perhaps you can seek redemption there. Be wary. Don't wander away from the trail; you will get lost." +
     " There are things in those woods that you don't want to see. Be careful.\n\n" +
     "She says this in a soft tone that it was almost mesmerizing for you to hear.\n\n" +
     "\tYOU: Will I see you at this red chapel?\n\n" +
     "\tHER: Perhaps...\n\n" +
     "\tYOU: I'll get to it then.\n\n",

     "have not":"\tYOU: I… I don't know. I can't say, it's… it's not coming to me.\n\n" +
     "You frown and lean back into the bench a little, searching desperately in your head for a possible reason. You then look back at the woman and have" +
     " the vague feeling that She's frowning at you despite being unable to see Her face.\n\n" +
     "\tHER: Perhaps… you are here for something deeper.\n\n" +
     "Her voice is a little darker, surprising you.\n\n" +
     "\tYOU: What do you mean?\n\n" +
     "\tHER, RESOLUTELY: Perhaps you are looking for redemption.\n\n" +
     "This doesn't make sense to you.\n\n" +
     "\tHER: Visit the red chapel in the black woods. Perhaps you can seek redemption there. Don't wander away from the trail; you will get lost. There are" +
     " things in those woods that you don't want to see.\n\n" +
     "Despite Her earlier tone, it is now soft and mesmerizing for you to hear.\n\n" +
     "\tYOU: Will I see you at this red chapel?\n\n" +
     "\tHER: Perhaps...\n\n" +
     "\tYOU: I'll get to it then.\n\n"
}

current_room = 0
inventory = []

def getDesc(room):
    return(room[current_room]["description"])

def getActions(room):
    for x in range(len(room[current_room]["actions"])):
        print("- ", room[current_room]["actions"][x])

def print_split_text():
    desc = getDesc(rooms)
    split_text = desc.split("\n\n")
    for x in range(len(split_text)):
        print(split_text[x])
        input()

# Instructions
print("INSTRUCTIONS: To get the next line of description or dialogue, please simply press ENTER.\n",
      "All player commands are case sensitive. Make sure to write the exact case sensitive command.\n\n")
input()

# Starting room
print_split_text()
getActions(rooms)

# Main game loop
running = True
while running:
    player_input = input("\n> ")

    match player_input:
        case "Look out the window":
            current_room = 1
            print()
            print_split_text()
            getActions(rooms)
        case "Look in the closet":
            current_room = 2
            print()
            print_split_text()
            getActions(rooms)
        case "Take the jacket":
            current_room = 3
            print()
            print_split_text()
            inventory.append("JACKET")
            print(">>> JACKET has been added to your inventory.\n\n")
            getActions(rooms)
        case "Search the jacket":
            current_room = 4
            print()
            print_split_text()
            getActions(rooms)
        case "Head out the room":
            current_room = 5
            state = 1
            print()
            print_split_text()
            getActions(rooms)
        # Go back to the starting room if you want
        case "Go back to the room":
            current_room = 0
            print()
            getActions(rooms)
        # Go back to the hallway
        case "Go back to the hallway":
            current_room = 5
            print()
            getActions(rooms)
        case "Open the door on the right":
            current_room = 6
            print()
            print_split_text()
            getActions(rooms)
        case "Search the bathroom":
            current_room = 7
            print()
            print_split_text()
            getActions(rooms)
        case "Open the door on the left":
            current_room = 8
            print()
            print_split_text()
            getActions(rooms)
        case "Search the office":
            current_room = 9
            print()
            print_split_text()
            getActions(rooms)
        case "Yes":
            # Case for "Search the office, take the burned picture?"
            if current_room == 9:
                current_room = 10
                print()
                inventory.append("1/3 OF BURNED PHOTO")
                print(">>> 1/3 OF BURNED PHOTO has been added to your inventory.\n\n")
                print_split_text()
                getActions(rooms)
            else:
                break
        case "No":
            # Case for "Search the office, take the burned picture?"
            if current_room == 9:
                current_room = 11
                print()
                print_split_text()
                getActions(rooms)
            else:
                break
        case "Enter the living room":
            current_room = 12
            print()
            print_split_text()
            getActions(rooms)
        # Go back to the living room if you want
        case "Go back to the living room":
            current_room = 12
            print()
            getActions(rooms)
        case "Go to the kitchen":
            current_room = 13
            print()
            print_split_text()
            getActions(rooms)
        case "Search the kitchen":
            current_room = 14
            print()
            print_split_text()
            getActions(rooms)
        case "Go to the backyard":
            current_room = 15
            print()
            print_split_text()
            getActions(rooms)
        case "Head outside and into town":
            current_room = 16
            print()
            print_split_text()
            getActions(rooms)
        case _:
            print("\n\nUnknown command. Try again.")
            # Exit game
            running = False
            # getActions(rooms)
