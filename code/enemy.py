#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.entity1 import Entity1


class Enemy(Entity1):
    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Remover entidade

