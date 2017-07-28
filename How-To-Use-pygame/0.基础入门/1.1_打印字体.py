import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))

white = (255,255,255)
blue = (0,0,200)
myfont = pygame.font.SysFont("arial",60)
textImage = myfont.render("Hello Pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            exit()

    screen.fill(blue)
    screen.blit(textImage, (100,100))
    pygame.display.update()