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

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load("H:\CP2/spaceInvaders/player/playerShipV4.png").convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey



'''
Setup
'''
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 400  # go to x
player.rect.y = 775  # go to y
"""
if player.rect.x < 0:
    player.rect.x = 0
if player.rect.x > 750:
    player.rect.x = 750
"""
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 5


'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if player.rect.x <= 0:
            player.rect.x = 0
        if player.rect.x >= 750:
            player.rect.x = 751
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)