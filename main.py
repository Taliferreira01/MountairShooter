# bem vindo ao python
import pygame
import pygame as pg

print('Setap start')
pygame.init()
# criar janela vamos criar uma variável chamada
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Start loop')
while True:  # laço de repetição mantém a janela aberta
    # check dor all events       evento para usar o fechar dp pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end pygame.
