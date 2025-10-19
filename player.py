import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 80))
        self.image.fill((50, 50, 50))
        self.rect  = self.image.get_rect()
        self.rect.center = (700, 350)
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.y < 15:
            self.rect.y = 15
        if self.rect.y >= 405:
            self.rect.y = 405
