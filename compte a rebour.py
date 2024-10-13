import pygame
import math
import partie

orange=(237,127,16)
black=(0,0,0)

background_color=(0,255,0)

compteur_color=orange
skibidi={10:'le',9:'caca',8:'c',7:'trop',6:'bon',5:'haha',4:'haha',3:'haha',2:'haha',1:'haha',0:'haha'}
haut=900
larg=1850

fps=1

pygame.init()


horloge=pygame.time.Clock()

fen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Compteur')
fen.fill(background_color)
police = pygame.font.Font(None,100)
compteur=10

#butn lance partie
play_button=pygame.image.load('asset/buton_joue.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect= play_button.get_rect()
play_button_rect.x = math.ceil(fen.get_width()/2)
play_button_rect.y = math.ceil(fen.get_height()/2)

#btn quitter
quit_but=pygame.image.load('asset/bouton_quit.png')
quit_but= pygame.transform.scale(quit_but,(100,100))
quit_but_rect=quit_but.get_rect()
quit_but_rect.x = math.ceil(fen.get_width()/2)

quit_but2=pygame.image.load('asset/bouton_quit.png')
quit_but2= pygame.transform.scale(quit_but,(200,100))
quit_but2_rect=quit_but2.get_rect()
quit_but2_rect.x = math.ceil(fen.get_width()/3)

is_playing=False


continuer=True
while continuer:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            continuer=False

    fen.fill(background_color)



    msg_compteur = police.render(f'{skibidi[compteur]}',True,compteur_color)
    fen.blit(quit_but,quit_but_rect)

    if is_playing==True:
        fen.blit(quit_but2,play_button_rect)
        if compteur<=0:
            is_playing=False
            compteur=10
        elif compteur_color==orange:
            compteur_color=black
        else:
            compteur_color=orange
        compteur-=1
        horloge.tick(fps)
        fen.blit(msg_compteur,(80,20))
        if event.type== pygame.MOUSEBUTTONDOWN:
                #verif souri colision buton play
                if quit_but2_rect.collidepoint(event.pos):
                    is_playing=False

    if is_playing==False:
        fen.blit(play_button,play_button_rect)
        if event.type== pygame.MOUSEBUTTONDOWN:
            #verif souri colision buton play
            if play_button_rect.collidepoint(event.pos):
                is_playing=True
        if event.type== pygame.MOUSEBUTTONDOWN:
                #verif souri colision buton play
                if quit_but_rect.collidepoint(event.pos):
                    continuer=False


    pygame.display.flip()

