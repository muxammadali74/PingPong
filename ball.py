import pygame
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 250)
        self.speed_x = random.choice([-6, 6])
        self.speed_y = random.choice([-4, 4])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 15 or self.rect.bottom >= 490:
            self.speed_y *= -1
