import pygame
pygame.init()
fps=30
screen_width=1000
screen_height=700
exit_game=False
screen=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
background=pygame.image.load('background1.png')
icon=pygame.image.load('icon1.png')
pygame.display.set_caption("SPACEHUB")
pygame.display.set_icon(icon)
pygame.display.update()

while not exit_game:
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.WINDOWRESIZED:
            background = pygame.transform.scale(background, (screen.get_width(),screen.get_height()))
            screen.blit(background, (0, 0))
            pygame.display.update()
pygame.quit()
quit()