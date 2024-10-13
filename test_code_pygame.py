# Ecrit ton programme ici ;-)
import pygame
# par la même occasion cela importe pygame.locals dans l'espace de nom de Pygame
def test():
    pygame.init()

    ecran = pygame.display.set_mode((300, 200))

    continuer = True

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                continuer = False

