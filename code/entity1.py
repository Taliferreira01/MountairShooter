#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity1(ABC):                #importar_classe_abstrata
    def __init__(self, name: str, postion: tuple):
        self.name = name
        self.surf = pygame.image.load('./Asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=postion[0], top=postion[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = "None"

    @abstractmethod
    def move(self, ):
        pass
