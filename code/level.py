#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity1 import Entity1


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode #modo de jogo
        self.entity_list: list[Entity1] = []

    def run(self, ):
        pass
