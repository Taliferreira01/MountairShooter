#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from code.entity1 import Entity1
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity1] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #pegar obj lista e jogar aqui dentro

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move() # invocar o movimento
            pygame.display.flip()
        pass
