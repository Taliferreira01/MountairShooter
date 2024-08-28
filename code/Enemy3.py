from code.enemy import Enemy
from code.Const import ENTITY_SPEED, WIN_HEIGHT


class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vertical_speed = ENTITY_SPEED[self.name]  # Normal vertical speed
        self.moving_down = True  # Start moving down

    def move(self):
        # Horizontal movement
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Vertical movement
        if self.moving_down:
            self.rect.centery += 2 * self.vertical_speed * 2
            if self.rect.bottom >= WIN_HEIGHT:
                self.moving_down = False
        else:
            self.rect.centery -= 2
            if self.rect.top <= 0:  # Bateu na borda superior
                self.moving_down = True
