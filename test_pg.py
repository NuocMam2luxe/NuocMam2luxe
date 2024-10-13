import pygame
from pygame.locals import *
class decompteur():
    def __init__(self):
        self.compte=10
    def decompte(self):
        if self>=0:
            self.compte=self.compte-1
        else:
            self.compte=10
objet=decompteur()

pygame.init()

fenetre = pygame.display.set_mode((1366, 768))
while True==True:
    objet.decompte
    print(object.compte)


font=pygame.font.Font(None, 24)
text = font.render(object.compte,1,(176,255,255))

continuer = 1

while continuer:

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

    fenetre.blit(text, (300, 300))

    pygame.display.flip()

pygame.quit()
