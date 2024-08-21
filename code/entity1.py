#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH


class Entity1(ABC):                #importar_classe_abstrata
    def __init__(self, name: str, postion: tuple):
        self.name = name
        self.surf = pygame.image.load('./Asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=postion[0], top=postion[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass
