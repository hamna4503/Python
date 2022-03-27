import random
import sys
import math
import pygame


pygame.init()
pygame.mixer.init()
fps=40
screen_width=900
screen_height=600
exit_game=False
clock=pygame.time.Clock()
black=(0,0,0)
screen=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
score=0

def iscollision(aestroid_1x, aestroid_1y, ship_x, ship_y):
    distance =abs( math.sqrt((math.pow(aestroid_1x - ship_x, 2) + math.pow(aestroid_1y - ship_y, 2))))
    if distance<= 70:
        return True
    else:
        return False

def gameover():
    over = pygame.image.load("game_obj/gameover.png")
    over = pygame.transform.scale(over, (screen.get_width(), screen.get_height())).convert_alpha()
    screen.blit(over, (0, 0))
    pygame.display.update()
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                sys.exit()
            if event.type == pygame.WINDOWRESIZED:
                over = pygame.transform.scale(over, (screen.get_width(), screen.get_height()))
                screen.blit(over, (0, 0))
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    gameloop()
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
                    sys.exit()


def title():
    icon = pygame.image.load('game_obj/icon1.png').convert_alpha()
    pygame.display.set_caption("SPACEHUB")
    pygame.display.set_icon(icon)
    welcome = pygame.image.load("game_obj/welcome.png")
    welcome = pygame.transform.scale(welcome, (screen.get_width(), screen.get_height())).convert_alpha()
    screen.blit(welcome, (0, 0))
    pygame.display.update()
    exit_game = False
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.WINDOWRESIZED:
                welcome = pygame.transform.scale(welcome, (screen.get_width(), screen.get_height()))
                screen.blit(welcome, (0, 0))
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    gameloop()
                if event.key==pygame.K_ESCAPE:
                    exit_game=True
                    sys.exit()
#main game loop
def gameloop():

    #gamevars
    fps = 40
    score=0
    exit_game = False
    clock = pygame.time.Clock()
    ship_x=3
    ship_y=250
    aestroid1_x=1500
    aestroid1_y=40
    aestroid2_x=1500
    aestroid2_y=20
    aestroid3_x=1500
    aestroid3_y=20

    #displayvars
    background=pygame.image.load('game_obj/background1.png').convert_alpha()
    icon=pygame.image.load('game_obj/icon1.png').convert_alpha()
    ship=pygame.image.load('game_obj/ship4.png').convert_alpha()
    ship = pygame.transform.scale(ship, (150,150)).convert_alpha()
    aestroid1=pygame.image.load('game_obj/aestroid.png').convert_alpha()
    aestroid1=pygame.transform.scale(aestroid1,(180,180)).convert_alpha()
    aestroid2=pygame.image.load('game_obj/aestroid.png').convert_alpha()
    aestroid2=pygame.transform.scale(aestroid2,(180,180)).convert_alpha()
    aestroid3=pygame.image.load('game_obj/aestroid.png').convert_alpha()
    aestroid3=pygame.transform.scale(aestroid3,(150,150)).convert_alpha()
    pygame.display.set_caption("SPACEHUB")
    pygame.display.set_icon(icon)
    pygame.display.update()

    #audio
    pygame.mixer.music.load("audio/main_audio2.mp3")
    pygame.mixer.music.set_volume(40)
    pygame.mixer.music.play(-1)
    whoosh=pygame.mixer.Sound("audio/whoosh.mp3")
    def displayship(x_shipfun,y_shipfun):
        screen.blit(ship, (x_shipfun, y_shipfun))

    while not exit_game:
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        displayship(ship_x, ship_y)
        screen.blit(aestroid1,(aestroid1_x,aestroid1_y))
        screen.blit(aestroid2, (aestroid2_x, aestroid2_y))
        screen.blit(aestroid3, (aestroid3_x, aestroid3_y))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                exit_game=True
                sys.exit()

            if event.type==pygame.WINDOWRESIZED:
                background = pygame.transform.scale(background, (screen.get_width(),screen.get_height()))
                screen.blit(background, (0, 0))
                pygame.display.update()

            if event.type== pygame.KEYDOWN:
               if event.key==pygame.K_DOWN:
                   pygame.mixer.Sound.play(whoosh)
                   ship_y+=45
               if event.key==pygame.K_UP:
                   ship_y-=45
                   pygame.mixer.Sound.play(whoosh)
               if event.key==pygame.K_RIGHT:
                   ship_x+=45
                   pygame.mixer.Sound.play(whoosh)
               if event.key==pygame.K_LEFT:
                   ship_x-=45
                   pygame.mixer.Sound.play(whoosh)
               if event.key==pygame.K_ESCAPE:
                   sys.exit()

        if aestroid1_x<=-100:
            screen.blit(background,(0,0))
            displayship(ship_x,ship_y)
            aestroid1_x=1500
            aestroid1_y=random.randint(-30,200)
            screen.blit(aestroid1,(aestroid1_x,aestroid1_y))
            pygame.display.update()

        if aestroid1_x>=1500:
            aestroid1_x_change=-18
        aestroid1_x+=aestroid1_x_change

        if aestroid2_x<=-100:
            screen.blit(background,(0,0))
            displayship(ship_x,ship_y)
            aestroid2_x=1500
            aestroid2_y=random.randint(350,570)
            screen.blit(aestroid2,(aestroid2_x,aestroid2_y))
            pygame.display.update()

        if aestroid2_x>=1500:
            aestroid2_x_change=-15
        aestroid2_x+=aestroid2_x_change

        if aestroid3_x<=-100:
            screen.blit(background,(0,0))
            displayship(ship_x,ship_y)
            aestroid3_x=1500
            aestroid3_y=random.randint(150,410)
            screen.blit(aestroid3,(aestroid3_x,aestroid3_y))
            pygame.display.update()

        if aestroid3_x>=1500:
            aestroid3_x_change=-8
        aestroid3_x+=aestroid3_x_change

        displayship(ship_x, ship_y)
        pygame.display.update()
        clock.tick(fps)
        collision = iscollision(aestroid1_x, aestroid1_y, ship_x, ship_y) \
                    or iscollision(aestroid2_x,aestroid2_y,ship_x,ship_y) or \
                    iscollision(aestroid3_x,aestroid3_y,ship_x,ship_y)
        if collision:
            pygame.mixer.music.fadeout(10)
            gameover()
        score+=0.025
        print(score)
title()
pygame.quit()
quit()





