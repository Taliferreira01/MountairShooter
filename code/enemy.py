#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity1 import Entity1


class Enemy(Entity1):
    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # CADA IMAGEM VAI SE MOVENDO
        if self.rect.right <= 3:  # MOVIMENTO DIRETO AX
            self.rect.left = WIN_WIDTH  # FAZER MOVIMENTO CONTINUO

