#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy3 import Enemy3
from code.background import Background
from code.enemy import Enemy
from code.player import Player



class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':  # Criou Level 1
                list_bg = []  # lista de background
                for i in range(7):  # bg level 1 image
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':  # Criou Level 2
                list_bg = []  # lista de background
                for i in range(5):  # bg level2 image
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level3Bg':  # Criou Level 3
                list_bg = []  # lista de background
                for i in range(5):  # bg level3 image
                    list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1':  # Criar player 1 . 1 jogador
                return Player('player1', (10, WIN_HEIGHT / 2 - 30))  # nome e posição
            case 'player2':  # Criar player 2 . 2 jogador
                return Player('player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Enemy3':
                return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
