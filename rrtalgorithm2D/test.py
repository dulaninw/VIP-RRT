import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

red = pygame.Color(255, 0, 0)
screen.fill(red)

while True:
    for event in pygame.event.get():
        pass

    pygame.display.update()