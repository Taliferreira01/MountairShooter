from code.Const import ENTITY_SPEED
from code.entity1 import Entity1


class PlayerShot(Entity1):

    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)

    def move(self, ):
        self.rect.centerx += ENTITY_SPEED[self.name]
