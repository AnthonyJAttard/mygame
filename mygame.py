#!/usr/bin/env python

import random
import sys
import time

import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Raspberry Snake')

# noinspection PyArgumentList,PyArgumentList
redColour = pygame.Color(255, 0, 0)
# noinspection PyArgumentList,PyArgumentList
blackColour = pygame.Color(0, 0, 0)
# noinspection PyArgumentList,PyArgumentList
whiteColour = pygame.Color(255, 255, 255)
# noinspection PyArgumentList,PyArgumentList
greyColour = pygame.Color(15, 150, 150)

snakePosition = [100, 100]
snakeSegments = [[100, 100], [80, 100], [60, 100]]
raspberryPosition = [300, 300]
raspberrySpawned = 1
directions = {K_LEFT: 'left', K_RIGHT: 'right', K_UP: 'up', K_DOWN: 'down'}
direction = directions[K_RIGHT]
changeDirection = direction


def game_over():
    game_over_font = pygame.font.Font('freesansbold.ttf', 72)
    game_over_surf = game_over_font.render('Game Over', True, greyColour)
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (320, 10)
    playSurface.blit(game_over_surf, game_over_rect)
    pygame.display.flip()
    time.sleep(5)
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = directions[K_RIGHT]
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = directions[K_LEFT]
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = directions[K_UP]
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = directions[K_DOWN]
            if event.key == K_ESCAPE:
                # noinspection PyArgumentList
                pygame.event.post(pygame.event.Event(QUIT))

    if changeDirection == directions[K_RIGHT] and not direction == directions[K_LEFT]:
        direction = changeDirection
    if changeDirection == directions[K_LEFT] and not direction == directions[K_RIGHT]:
        direction = changeDirection
    if changeDirection == directions[K_UP] and not direction == directions[K_DOWN]:
        direction = changeDirection
    if changeDirection == directions[K_DOWN] and not direction == directions[K_UP]:
        direction = changeDirection

    if direction == directions[K_RIGHT]:
        snakePosition[0] += 20
    if direction == directions[K_LEFT]:
        snakePosition[0] -= 20
    if direction == directions[K_UP]:
        snakePosition[1] -= 20
    if direction == directions[K_DOWN]:
        snakePosition[1] += 20

    snakeSegments.insert(0, list(snakePosition))

    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    else:
        snakeSegments.pop()

    if raspberrySpawned == 0:
        x = random.randrange(1, 32)
        y = random.randrange(1, 24)
        raspberryPosition = [x * 20, y * 20]
        raspberrySpawned = 1

    playSurface.fill(blackColour)
    for position in snakeSegments:
        pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))
    pygame.draw.rect(playSurface, redColour, Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
    pygame.display.flip()

    if snakePosition[0] > 620 or snakePosition[0] < 0:
        game_over()
    if snakePosition[1] > 460 or snakePosition[1] < 0:
        game_over()

    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            game_over()

    fpsClock.tick(20)
