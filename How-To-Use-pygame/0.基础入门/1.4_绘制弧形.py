import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            exit()

    screen.fill((0, 0, 200))

    # 绘制弧形的代码
    pink = (255, 0, 255)
    color = pink
    position = (0, 0, 400, 400)#为弧提供 矩形边界 参数，所以是2个点，呈对角分布
    start_angle = math.radians(0)#将角度转化为弧度
    end_angle = math.radians(180)
    width = 8
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    pygame.display.update()