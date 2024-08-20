#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case'Level1Bg': #Criou Level 1
                list_bg= [] #lista de background
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0)))
                return list_bg
            case 'player1': #Criar player 1 . 1 jogador
                return Player('player1',(10,WIN_HEIGHT / 2 - 30 )) #nome e posição
            case 'player2':  # Criar player 1 . 1 jogador
                return Player('player2', (10, WIN_HEIGHT / 2 + 30))






