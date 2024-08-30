#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Score import Score
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:  # laço de repetição mantém a janela aberta
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # player1, player2
                level = Level(self.window, 'Level1', menu_return, player_score)  # chamada level1
                level_return = level.run(player_score)
                if level_return:  # level_return == True.
                    level = Level(self.window, 'Level2', menu_return, player_score)  # chamada level2
                    level_return = level.run(player_score)
                    if level_return:  # caso passe a fase, salve score
                        level = Level(self.window, 'Level3', menu_return, player_score)  # chamada level2
                        level_return = level.run(player_score)

                        score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()  # fechar
            else:
                pass
