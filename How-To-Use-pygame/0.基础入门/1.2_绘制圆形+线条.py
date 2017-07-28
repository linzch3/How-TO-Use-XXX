import pygame

pygame.init()

screen = pygame.display.set_mode((600,500))
yellow = 255,255,0
position = 300,250
radius = 100
width = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# 接收到退出事件后退出程序
            pygame.quit()
            exit()

    screen.fill(0)
    pygame.draw.circle(screen, yellow, position, radius, width)
    # 绘制线条
    begin = (100,100)
    end = (500,400)
    pygame.draw.line(screen, yellow, begin, end, width)

    pygame.display.update()