# -*-coding:utf-8-*- s = '
#AoDaMiao Like Eating Fish
import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("嗷大喵爱吃鱼！")
font1 = pygame.font.SysFont("arial",34)
font2 = pygame.font.SysFont("arial",34)
font3 = pygame.font.SysFont("arial",34)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0
cat=pygame.image.load("aodamiao_2.png")
width,height=cat.get_size()
#pic=pygame.transform.smoothscale(cat,(width//2,height//2))
pic=pygame.transform.scale(cat,(width,height))
fish=pygame.image.load("fish.png")
width,height=fish.get_size()
fish=pygame.transform.smoothscale(fish,(width//3,height//3))
init=pygame.image.load("init.png")
lives = 10
score = 0
clock_start = 0
game_over = 1
mouse_x = mouse_y = 0
Round =1
mine=0
mine_png=pygame.image.load("mine.png")
cat2=pygame.image.load("aodamiao_3.png")
flag=0

pos_x = 300
pos_y = 410-40

bomb_x = random.randint(0,500)
mine_x=random.randint(0,500)
bomb_y = -50
vel_y = 0.4
vel_yy=0.6
mine_y=-100

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 10
                score = 0
                Round =1
                vel_y=0.4
                mine=0
                flag=0
                pic=cat

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,0,100))

    if game_over:
        screen.blit(init,(60, 60))
        print_text(font3, 200, 400,"Clicked To Play!")
        print_text(font2, 310, 480,"Copyright@2015 developed by xiaoxiami")
    else:
        #Round setting
        if score >300 and score <600:
             Round=2
        elif score >600 and score <900:
             Round =3
        elif score >900 and score <1200:
             Round=4
        elif score >1200 and score <1500:
             Round =5
        elif score >=1500:
             Round =6
        #draw the Round
        print_text(font1, 280, 0, "Round: " + str(Round))
        #speed setting
        if Round ==1:
            vel_y=0.4
        elif Round ==2:
            vel_y=0.6
        elif Round ==3:
            vel_y=0.8
        elif Round ==4:
            vel_y=1.0
        elif Round ==5:
            vel_y=1.2
        #mine number setting
        #mine=random.randint(1,9)
        #move the fish
        bomb_y += vel_y
        mine_y+=vel_yy

        #has the player missed the fish?
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
        #see if player has caught the fish
        elif bomb_y > pos_y:
            if bomb_x > pos_x-10 and bomb_x < pos_x + 70:
                score += 10
                bomb_x = random.randint(0, 500)
                bomb_y = -50
        if Round >2:
        #has the player missed the mine?
            if mine_y > 500:
                mine_x = random.randint(0, 500)
                mine_y = -50
        #see if player has caught the mine
            elif mine_y > pos_y:
                if mine_x > pos_x and mine_x < pos_x + 40:
                    mine_x = random.randint(0, 500)
                    mine_y = -50
                    lives-=1
                    pic=cat2
                    if lives == 0:
                        game_over = True
       
        #draw the fish
        screen.blit(fish,(bomb_x,int(bomb_y)))
        #draw the mine
        if Round >2:
            screen.blit(mine_png,(mine_x,int(mine_y)))

        #set cat position
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 510:
            pos_x = 500
        #draw cat
        if lives<5:
            pic=cat2
        screen.blit(pic,(pos_x,pos_y))

    #print # of lives
    print_text(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    print_text(font1, 500, 0, "SCORE: " + str(score))
    
    pygame.display.update()

    

