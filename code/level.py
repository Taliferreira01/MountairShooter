#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION
from code.entity1 import Entity1
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity1] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #imagem level1
        self.entity_list.append(EntityFactory.get_entity('player1')) #colocar a nave no jogo
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))
        self.timeout = 20000  # 20segundos

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # executar num tempo especifico

        while True:
            clock.tick(60)  # FPS
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()  # invocar o movimento
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # evento fechar janela
                    pygame.quit()
                    sys.exit()
            # printed text

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE,
                            (10, 5))  # tempo duração da fase
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))  # print clock na tela
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))  # quantas entidades na tela
            pygame.display.flip()

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
