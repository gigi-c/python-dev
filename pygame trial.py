import pygame

# Iniyialise the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Space Invaders")
# icon = pygame.image.load("ufo.png")
# pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB = red, green, blue (0 - 255)
    screen.fill((0, 0, 0))
    pygame.display.update()