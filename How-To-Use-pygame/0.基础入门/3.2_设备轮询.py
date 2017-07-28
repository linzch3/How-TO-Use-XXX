import pygame
import sys
from pygame.locals import *

pygame.init()
keys = pygame.key.get_pressed()
'''键盘轮询'''
while True:
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
'''在pygame中，使用pygame.key.get_pressed()来轮询键盘接口。
这个方法会返回布尔值的一个列表，其中每个键一个标志。使用键常量值来匹配按键，
这样的好处就是不必遍历事件系统就可以检测多个键的按下'''

#############################################3
'''鼠标轮询

同样，我们可以使用类似的方法去轮询鼠标事件。

这里有3个相关的函数：

（1）pygame.mouse.get_pos()，这个函数会返回鼠标当前的坐标x,y；

（2）pygame.mouse.get_rel();

rel_x ,rel_y = pygame.mouse.get_rel().利用这个函数可以读取鼠标的相对移动。

（3）btn_one,btn_two,btn_three = pygame.mouse.get_pressed();

利用这个函数，可以获取鼠标按钮的状态。比如当左键按下的时候btn_one 的值会被赋值为1，鼠标按键弹起是会被赋值为0。'''