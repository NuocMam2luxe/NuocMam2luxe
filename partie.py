import pygame

class joueur(pygame.sprite.Sprite):

    def __init__(self,x,y,taille):

        super().__init__()
        self.x=x
        self.y=y
        self.taille=taille
        self.rect=pygame.Rect(self.x,self.y,self.taille[0],self.taille[1])

    def afficher(self,surface):
        pygame.draw.rect(surface,(0,0,0),self.rect)

    def mouv(self,vitX,vitY):
        self.rect.x+=vitX
        self.rect.y+=vitY
