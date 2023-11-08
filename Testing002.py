import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up Pygame window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Text-Based Game with Pygame")

# Define game variables
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
background_color = (0, 0, 0)
text_x = 20
text_y = 20

# Define your game state variables and actions
state = 0
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(background_color)

    # Your text-based content
    text = "Purgatory" 

    # Render and display the text
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (text_x, text_y))

    # Update the display
    pygame.display.flip()

