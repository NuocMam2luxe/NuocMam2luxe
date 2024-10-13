import pygame
import math
from partie import joueur

orange=(237,127,16)
black=(0,0,0)

background_color=(0,255,0)


mec=joueur(600,200,(32,64))
mec_vitX=1
mec_vitY=0

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
    touches = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            continuer=False

    fen.fill(background_color)


    if is_playing==True:
        fen.blit(quit_but2,quit_but2_rect)
        mec.afficher(fen)
        print(event)

    if event.type== pygame.KEYDOWN:
        if event.type==pygame.K_q:
            mec_vitX-=1
    elif event.type== pygame.KEYUP:
        if event.type==pygame.K_q:
            mec_vitX=0


    if event.type== pygame.KEYDOWN:
        if event.type==pygame.K_d:
            mec_vitX=1
    if event.type== pygame.KEYUP:
        if event.type==pygame.K_d:
            mec_vitX=0


    if event.type== pygame.KEYDOWN:
        if event.type==pygame.K_s:
            mec_vitY=1
    if event.type== pygame.KEYUP:
        if event.type==pygame.K_s:
            mec_vitY=0


    if event.type== pygame.KEYDOWN:
        if event.type==pygame.K_z:
            mec_vitY-=1
    if event.type== pygame.KEYUP:
        if event.type==pygame.K_z:
            mec_vitY=0

    if event.type== pygame.MOUSEBUTTONDOWN:
        #verif souri colision buton play
        if quit_but2_rect.collidepoint(event.pos):
            is_playing=False


    if is_playing==False:
        fen.blit(quit_but,quit_but_rect)
        fen.blit(play_button,play_button_rect)
        if event.type== pygame.MOUSEBUTTONDOWN:
            #verif souri colision buton play
            if play_button_rect.collidepoint(event.pos):
                is_playing=True
        if event.type== pygame.MOUSEBUTTONDOWN:
                #verif souri colision buton play
                if quit_but_rect.collidepoint(event.pos):
                    continuer=False

    mec.mouv(mec_vitX,mec_vitY)
    pygame.display.flip()

