#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.PlayerShot import PlayerShot
from code.entity1 import Entity1


class Player(Entity1):
    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):  # Movimento NAVE
        pressed_key = pygame.key.get_pressed()  # enquanto a tecla for pressionada self.name seleciona o player movimentado
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # vai subir e parar quando o y cegar a 0
            self.rect.centery -= ENTITY_SPEED[self.name]  # mexer posição da nave y e velocidade player1
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:  # enquanto for menor que WIN, vai descer
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # mover para esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:  # Movimento direta
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', postion=(self.rect.centerx, self.rect.centery))
