import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1
blue = (0,0,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            exit()

    screen.fill(blue)#绘制背景颜色为蓝色

    # 移动矩形
    pos_x += vel_x
    pos_y += vel_y

    # 使矩形保持在窗口内
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x     #将vel_*置反，可显示出碰撞后反弹的效果
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    # 绘制矩形
    color = (255, 255, 0) #黄色
    solid = 0  # 实体填充
    pos = (pos_x, pos_y, 100, 100)
    pygame.draw.rect(screen, color, pos, solid)
    #更新
    pygame.display.update()