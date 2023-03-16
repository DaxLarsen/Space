#import modules(Key)
#922E2E
from typing import Tuple
import random
import threading
import pygame
import sys
import os
import time
from time import sleep
import math




#Loading
rocketship = ("Rocket ship is not a cult. It is a way of life.", "Remember, if you don’t kill all the aliens, you will die!", "Rocket ship has taken over. Please help.", "Barriers are there to help you! Use them to your advantage!", "You’ve got this!", "Don’t be a mass alien murderer! Or do, I don’t care.", "Don’t disappoint Rocket ship. Please.", "Cheese doesn’t exist in space!", "Rocket ship is choosing a new vessel. Beware.", "The blood of the aliens is rain on the earth.", "You might be made out of stardust, but Rocket ship is made out of ???.", "The person writing these tips has been left alone for too long. Cheese.", "Possession is lit! Try it on your friends today!", "I used to be a child. Now I’m just Rocket ship.", "The smaller the star, the less it lives! Just like you…", "Rocket ship wants to play…", "The sun is hot! Don’t touch it!", "What do aliens use to fuel their rocket ships? I mean, they didn’t have dinosaurs…", "Black holes don’t suck. They’re actually pretty cool.", "Don’t leave me alone, please. I need to escape this monster.", "Want to play a game? It’s called… Rocket ship.", "Rocket ship is watching. Always watching.", "Key is a disappointment. It’s fine, Rocket ship will find a new vessel.", "Don’t ask where Rocket ship gets it’s food. That’s a secret.", "Don’t talk to the humans in the basement. They’re scary.", "I used to stare at the stars and wish I could be there. Now I just want to go home…", "Why did you hurt me? I just want to be a kid again…", "Enjoy life while you can, kid…","You left me alone… now all that’s left is Rocket ship.")


#loaded = 0
#loading = True
#msg = "loading.."
#tip = random.choice(rocketship)
#while loading:
    #for x in range(10):
        #os.system('cls')
        #print(msg)
        #print(tip)
        #msg = msg + "."
        #loaded += 1
        #sleep(1)
        #if loaded == 2 or loaded == 4 or loaded == 6 or loaded == 8:
            #tip = random.choice(rocketship)
            #msg = "loading.."
        #elif loaded == 10:
            #loading = False
            #os.system('cls')
           
#Set color values: (Key)
BLUE = (25, 25, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TITLE = (199, 88, 74)
ALPHA = (0, 255, 0)


#Set World Values: (Daxton/Key)
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


#Player Sprite: (Daxton)
playerimg = pygame.image.load("H:\CP2/spaceInvaders/player/playerShipV6.png")
playerX = 500
playerY = 725
playerX_change = 0

def player(x,y):
    world.blit(playerimg, (x,y))

#Bullet:(Daxton)
    #If bullet does not hit anything reset reload after deleting bullet.
#If bullet hits brick; destroy brick, and reset reload.
#If bullet hits bomb; destroy bomb, add 5 points to score, and reset reload.
#If bullet hits alien; destroy alien, add 20 points to score, and reset reload.
    #If multiple of 8 aliens are killed, add 3 to move down counter
#If bullet hits ship; destroy ship, add 100 points to score, and reset reload.

bulletimg = pygame.image.load("H:\CP2/spaceInvaders/player/bullet/bulletV2.png")
bulletX = 0
bulletY = 725
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"

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


#Enemy:(Key/Daxton)

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

def enemy(x,y,i):
    global num_of_enemies
    world.blit(enemyimg[i], (x,y))


    #Bomb:
        #If bomb hits brick destroy bricks, more than player does
        #If bomb hits player, player loses life
        #If player has a life continue wave
        #If not game over screen
    #Alien:
        #Movement:
            #Move left until barrier, then move right
            #Move right until barrier, then move left
            #Move down after 15-20 movements
        #Billy


        #If all Aliens are defeated:
            #Win screen
            #Reset wave with faster Aliens
    #Ship:
        #Move left if coming from right
        #Move right if coming from left




#When New Wave:(Key)
        #Reset bricks
        #Alien bullet speed gets faster
        #If multiple of 10 waves player speed gets faster
        #If multiple of 5 waves player bullet gets faster
        #When that wave reaches 1 minute, alien speed gets faster
        #When that wave reaches 1 minute, alien bullet speed gets faster
#Scoreboard:(Key)  
        #Display score
        #If score 4000 points add life
        #Add score to scoreboard


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






#Instructions:(Key)
pygame.display.set_caption('Show Text')


font1 = pygame.font.Font('H:\CP2/spaceInvaders/Gamer.ttf', 30)


text1 = font1.render("Press 'q' to quit game", True, WHITE)
text2 = font1.render("Press 'a' or left arrow key to go left", True, WHITE,)
text3 = font1.render("Press 'd' or right arrow key to go right", True, WHITE,)
text4 = font1.render("Press 'w', spacebar, or up arrow key to shoot a bullet", True, WHITE,)


textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()


textRect1.center = (worldx // 13.2, worldy // 46)
textRect2.center = (worldx // 8.7, worldy // 24)
textRect3.center = (worldx // 8.1, worldy // 16)
textRect4.center = (worldx // 6, worldy // 12)


#title: (Key)
font2 = pygame.font.Font('H:\CP2/spaceInvaders/Gamer.ttf', 80)


text5 = font2.render("Space Invaders", True, TITLE)


textRect5 = text5.get_rect()


textRect5.center = (worldx // 2, worldy // 30)


#tips: (Amelia/Key)
font3 = pygame.font.Font('H:\CP2/spaceInvaders/Gamer.ttf', 30)


text6 = font3.render(random.choice(rocketship), True, WHITE)


textRect6 = text6.get_rect()


textRect6.center = (worldx // 2, worldy // 1.05)


#Setup: (Daxton/Key)
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True


#Game Loop (All)
while main:


    #Create Backdrop Color
    world.fill(BLACK)
   
    #Load Text
    world.blit(text1, textRect1)
    world.blit(text2, textRect2)
    world.blit(text3, textRect3)
    world.blit(text4, textRect4)
    world.blit(text5, textRect5)
    world.blit(text6, textRect6)


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

