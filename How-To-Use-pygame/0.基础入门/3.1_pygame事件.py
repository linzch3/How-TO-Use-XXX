import pygame
import sys
from pygame.locals import *


while True:
    #实时事件循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 接收到退出事件后退出程序
            pygame.quit()
            exit()
'''代码将会创建当前等待处理的事件的一个列表，然后使用for循环来遍历里面的事件。
这样，我们将会根据事件产生的顺序依次地进行不同的操作。常见的事件是按键按下，
按键释放以及鼠标移动。
通常需要最先处理QUIT事件（在用户关闭窗口的时候会产生该事件。）'''

while True:
    #键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_flag = True
        elif event.type == pygame.KEYUP:
            key_flag = False
'''键盘事件包括最典型的keyup 和 keydown 当按键按下的时候响应KEYDOWN事件，
按键弹起的时候响应KEYDOWN事件。
通常可以设置一个事件变量，然后根据keyup或者keydown给它赋不同的值。'''

################################################################
'''默认的话pygame不会重复地去响应一个被一直按住的键，
  只是在按键第一次被按下的时候响应一次，如果需要重复响应一个按键的话,见下面的操作：'''
pygame.key.set_repeat(10)#参数是一个以毫秒为单位的值
################################################################

#鼠标事件
'''pygame支持一些鼠标事件，他们包括MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN.'''
for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
        mouse_x, mouse_y = event.pos
        move_x, move_y = event.rel