import pygame
from pygame.locals import*
import random
import sys
pygame.init()
fps=30
screen_width=1000
screen_height=760
exit_game=False
screen=pygame.display.set_mode((screen_height,screen_width))
clock=pygame.time.Clock
player='ship1.png'
background='background1.png'
welcome='b.png'
game_over='gameover.png'
icon=pygame.image.load('icon1.png')

while not exit_game:
    pygame.display.set_caption("SPACEHUB")
    pygame.display.set_icon(icon)
    pygame.display.update()


pygame.quit()
quit()