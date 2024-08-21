from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity1 import Entity1


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
    def verify_collision(entity_list: list[Entity1]):  # gerenciar colisões
        for i in range(len(entity_list)):  #verificar entidade por entidade e desparecer
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity1]): #pegando cada entidade, se a vida for <= 0 remove
        for ent in entity_list: #destruir a entidade
            if ent.health <=0:
                entity_list.remove(ent)
