from typing import Tuple

import pygame
import sys
import os
import random
import math

'''
Variables
'''

worldx = 1200
worldy = 900
fps = 100
ani = 4
x = 0
y = 0
world = pygame.display.set_mode([worldx, worldy])
pygame.display.set_caption("Rocket Ship")
icon = pygame.image.load("H:\CP2/spaceInvaders/baby.png")
pygame.display.set_icon(icon)
pygame.font.init()

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''

playerimg = pygame.image.load("H:\CP2/spaceInvaders/player/playerShipV6.png")
playerX = 500
playerY = 725
playerX_change = 0

enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 30

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("H:\CP2/spaceInvaders/enemies/BillyV5.png"))
    enemyX.append(random.randint(0,1057))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.3)
    enemyY_change.append(50)


bulletimg = pygame.image.load("H:\CP2/spaceInvaders/player/bullet/bulletV2.png")
bulletX = 0
bulletY = 725
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('H:\CP2/spaceInvaders/Gamer.ttf', 50)
winFont = pygame.font.Font("H:\CP2/spaceInvaders/BloodyScript.ttf", 150)
loseFont = pygame.font.Font("H:\CP2/spaceInvaders/Gamer.ttf", 150)
textX = 970
textY = 850
winX = 380
winY = 300
loseX = 380
loseY = 300


def show_score(x,y):
    score = font.render("Score : " + str(score_value),True, (255,255,255))
    world.blit(score, (x,y))

def show_win(x,y):
    win = winFont.render("You Win",True, (146,46,46))
    world.blit(win, (x,y))

def show_lose(x,y):
    lose = loseFont.render("Game Over",True, (146,46,46))
    world.blit(lose, (x,y))

def player(x,y):
    world.blit(playerimg, (x,y))

def enemy(x,y,i):
    global num_of_enemies
    world.blit(enemyimg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    world.blit(bulletimg, (x + 42,y - 40))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 40:
        return True
    else:
        return False


'''
Setup
'''
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

'''
Main Loop
'''

while main:
    world.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT:
                playerX_change = -1.9
            if event.key == pygame.K_a:
                playerX_change = -1.9
            if event.key == pygame.K_RIGHT: 
                playerX_change = 1.9
            if event.key == pygame.K_d:
                playerX_change = 1.9
            if event.key == pygame.K_UP:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)
            if event.key == pygame.K_w:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w:
                playerX_change = 0

        

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1108:
        playerX = 1108

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1157:
            enemyX_change[i] = -1.3
            enemyY[i] += enemyY_change[i]

        collision = isCollision (enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 725
            bullet_state = "ready"
            score_value += 20
            enemyX[i] = random.randint(0,1057)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)


        if enemyY[i] >= playerY:
            show_lose(loseX,loseY)
            pygame.quit

        

    if bulletY <= 0:
        bulletY = 725
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    if score_value >= 1000:
        show_win(winX,winY)
    
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    pygame.display.flip()

    clock.tick(fps)