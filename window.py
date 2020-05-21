import pygame, sys
pygame.init()
window = pygame.display.set_mode((800, 650))
pygame.display.set_caption("chessApp")
window.fill((128, 0, 0))

playGame = True

# Loop for creating and exiting the window
while playGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playGame = False
    pygame.display.flip()