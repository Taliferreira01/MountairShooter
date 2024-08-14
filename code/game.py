#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
       pygame.init()
       self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):

        while True:  # laço de repetição mantém a janela aberta
            menu = Menu(self.window)
            menu.run()
            pass



            # check dor all events       evento para usar o fechar dp pygame
            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()  # close window
               #     quit()  # end pygame.
