from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity1 import Entity1
from code.player import Player


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity1):  # vereficar entidade na janela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent_one, ent_two):
        valid_interaction = False  # se colisão é validade entre entidades
        if isinstance(ent_one, Enemy) and isinstance(ent_two, PlayerShot):
            valid_interaction = True
        elif isinstance(ent_one, PlayerShot) and isinstance(ent_two, Enemy):
            valid_interaction = True
        elif isinstance(ent_one, Player) and isinstance(ent_two, EnemyShot):
            valid_interaction = True
        elif isinstance(ent_one, EnemyShot) and isinstance(ent_two, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction == True
            if (ent_one.rect.right >= ent_two.rect.left and
                    ent_one.rect.left <= ent_two.rect.right and
                    ent_one.rect.bottom >= ent_two.rect.top and
                    ent_one.rect.top <= ent_two.rect.bottom):
                ent_one.health -= ent_two.damage
                ent_two.health -= ent_one.damage
                ent_one.last_dmg = ent_two.name  # pontuar dano causado
                ent_two.last_dmg = ent_one.name

    @staticmethod
    def __give_socre(enemy: Enemy, entity_list: list[Entity1]):  # criar score
        if enemy.last_dmg == 'player1Shot':
            for ent in entity_list:
                if ent.name == 'player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'player2Shot':
            for ent in entity_list:
                if ent.name == 'player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity1]):  # gerenciar colisões
        for i in range(len(entity_list)):  # verificar entidade por entidade e desparecer
            entity_one = entity_list[i]
            EntityMediator.__verify_collision_window(entity_one)  # verificar se esta na janela e cair fora
            for j in range(i + 1, len(entity_list)):  # verificar colisão entre entidades
                entity_two = entity_list[j]
                EntityMediator.__verify_collision_entity(entity_one, entity_two)  # invocando

    @staticmethod
    def verify_health(entity_list: list[Entity1]):  # pegando cada entidade, se a vida for <= 0 remove
        for ent in entity_list:  # destruir a entidade
            if ent.health <= 0:
                if isinstance(ent, Enemy):  # Score
                    EntityMediator.__give_socre(ent, entity_list)  # quem matou
                entity_list.remove(ent)
