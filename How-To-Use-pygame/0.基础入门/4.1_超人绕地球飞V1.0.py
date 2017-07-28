import sys, random, math, pygame
from pygame.locals import *


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self): return self.__x

    def setx(self, x): self.__x = x

    x = property(getx, setx)

    # Y property
    def gety(self): return self.__y

    def sety(self, y): self.__y = y

    y = property(gety, sety)


def wrap_angle(angle):
    return angle % 360


radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("星空")
font = pygame.font.SysFont("arial", 18)

space = pygame.image.load("space.png").convert_alpha()
planet = pygame.image.load("earth.png").convert_alpha()
superman = pygame.image.load("superman.png").convert_alpha()
width, height = superman.get_size()
superman = pygame.transform.smoothscale(superman, (width // 2, height // 2))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.blit(space, (0, 0))

    angle = wrap_angle(angle - 0.1)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius

    # 获取位图的宽和高
    width, height = planet.get_size()
    # 在屏幕的中间绘制地球
    screen.blit(planet, (400 - width / 2, 300 - height / 2))
    width, height = superman.get_size()
    screen.blit(superman, (400 + pos.x - width // 2, 300 + pos.y - height // 2))
    pygame.display.update()