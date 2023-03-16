from typing import Tuple

import pygame
import sys
import os

'''
Variables
'''

worldx = 900
worldy = 900
fps = 100
ani = 4
world = pygame.display.set_mode([worldx, worldy])


BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load("H:\CP2/spaceInvaders/enemies/Jeffery.png").convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey



clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

enemy = Enemy()  # spawn enemy
enemy.rect.x = 400  # go to x
enemy.rect.y = 50  # go to y
if enemy.rect.x < 0:
    enemy.rect.x = 0
if enemy.rect.x > 750:
    enemy.rect.x = 750
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
steps = 5

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if enemy.rect.x <= 0:
            enemy.rect.x = 0
        if enemy.rect.x >= 750:
            enemy.rect.x = 751
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False

    enemy.update()
    enemy_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)