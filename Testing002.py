# Currently, this is not playable. I have only some of the map laid out that may or may not be properly utilized considering certain choices that aren't
# really designed for a map. It's something for now.

import pygame

rooms = [
    {
        # Beginning room, ACT 1: SCENE 1
        "description":"You wake up from a nightmare, sitting straight up in your bed. Your skin is slicked with sweat, and your heart pounds in your chest.\n\n" +
        "You can't recall the specific details of the nightmare.\n\n" +
        "     YOU: It was just a nightmare...\n\n" +
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
         "     YOU: Damn, guess I forgot to clean up. It's messy around here.\n\n" +
         "The couch is covered in soot, and the windows are all bare of their curtains. The walls are blackened with a substance.\n\n" +
         "     YOU: I could never get those stains to come out... Dunno what it is.\n\n" +
         "Adorning the walls are burned picture frames whose contents are blurred or burned or smudged away.\n\n" +
         "     YOU: Could never remember what they were.\n\n" +
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
         "     YOU: Wonder if my sense of smell finally got snuffed out.\n\n" +
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
         "     YOU: I wonder what that was...\n\n",
         
         "actions":["Go back to the living room"]
     },
     {
         # Head outside and into town
         "description":"You head to the front door, grab your keys hanging on the key holder beside it, and go outside. You survey the small" +
         " suburban neighborhood where replicas of your own house are repeated throughout the whole street.\n\n" +
         "     YOU: Weird. There's usually kids screaming outside at this hour.\n\n" +
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
         "     YOU: Hey there, miss... Are they... holding a wedding today?\n\n" +
         "     HER: Hello...\n\n" +
         "She says your name, much to your surprise.\n\n" +
         "     YOU: How do you know my name?\n\n" +
         "You don't recognize Her.\n\n" +
         "     HER: You simply seem like one...\n\n" +
         "     HER: No, there's no wedding today.\n\n" +
         "     YOU: What's with the dress then? If you don't mind me asking.\n\n" +
         "She softly chuckles.\n\n" +
         "     HER: It's simply a fashion choice. How have you been lately?" +
         "You don't notice the subject change.\n\n" +
         "     YOU: I... Well, to be honest, I've been pretty tired lately. I don't know why though.\n\n" +
         "     HER: Is it something personal? Or more of a workplace thing?\n\n" +
         "You feel like this woman is familiar, someone to be trusted. Her voice is soft and soothing, and you find conversing with Her easy.\n\n" +
         "     YOU: I think it might be more of a personal thing.\n\n" +
         "     HER: I see… Have you thought about finding solace in your community?\n\n" +
         "You look at the church with a skeptical expression. You purse your lips and try to remain as cordial as possible.\n\n" +
         "     YOU: If you mean religion, I'm afraid I'm not very religious. I don't… I don't really believe in God, ma'am.\n\n" +
         "She laughs, though it doesn't seem like She moves much at all.\n\n" +
         "     HER: That's fine...\n\n" +
         "She says your name again, and you feel more comfortable around Her.\n\n" +
         "     HER: Humor me a little... Join me in the church?\n\n",

         "actions":["Yes", "No"]
     }
]

def blit_text(surface, text, position, font, color=(255, 255, 255)):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = position
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = position[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = position[0]
        y += word_height

# Main game loop
def main():
    # Initialize pygame
    pygame.init()

    # Setting the screen dimensions
    screen = pygame.display.set_mode((800, 600))

    # Set the screen title
    pygame.display.set_caption("Purgatory")

    current_room = 0
    inventory = []

    font = pygame.font.SysFont('Arial', 24)

    # Displaying the current room
    blit_text(screen, rooms[current_room]["description"], (20, 20), font)

    # Displaying the actions for the room
    for i, action in enumerate(rooms[current_room]["actions"]):
        blit_text(screen, action, (20, 500 + 30 * i), font)

    try:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
