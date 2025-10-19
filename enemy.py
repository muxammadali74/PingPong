import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 80))
        self.image.fill((150,150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 350)
        self.speed = 3

    def update(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.rect.y += self.speed
        elif self.rect.centery > ball.rect.centery:
            self.rect.y -= self.speed

        if self.rect.y < 15:
            self.rect.y = 15
        if self.rect.y > 405:
            self.rect.y = 405

