#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png') #carregou a imagem
        self .rect = self.surf.get_rect(left=0, top=0) # criou o retangulo


    def run(self, ):
        pygame.mixer_music.load('./asset/fase1.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # imagem tem que aparecer no retang
            pygame.display.flip()  # atualizar na tela

            # check dor all events       evento para usar o fechar dp pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame.



