import time

import pygame

from PingPong.ball import Ball
from PingPong.config import WIDTH, HEIGHT, BLACK, FPS
from PingPong.enemy import Enemy
from PingPong.player import Player

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PingPong")
clock = pygame.time.Clock()

# --- Спрайты ---
all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
ball = Ball()
all_sprites.add(player, enemy, ball)

# --- Шрифт и счёт ---
pause_time = 0
player_score = 0
enemy_score = 0
font = pygame.font.SysFont(None, 48)
title_text = font.render("SCORE", False, (0, 255, 0))

def draw_map(surface):
    pygame.draw.line(surface, (38,117,22), (0, 10), (800, 10), 5)
    pygame.draw.line(surface, (38,117,22), (10, 10), (10, 490), 5)
    pygame.draw.line(surface, (38,117,22), (790, 10), (790, 490), 5)
    pygame.draw.line(surface, (38,117,22), (0, 490), (800, 490), 5)

running = True
while running:
    # --- События ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Обновление ---
    player.update()
    if time.time() > pause_time:
        ball.update()
    enemy.update(ball)

    if pygame.sprite.collide_rect(ball, player) or pygame.sprite.collide_rect(ball, enemy):
        ball.speed_x *= -1

    if ball.rect.left <= 0:
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        ball.speed_x *= -1
        player_score += 1
        pause_time = time.time() + 1

    if ball.rect.right >= WIDTH:
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        ball.speed_x *= -1
        enemy_score += 1
        pause_time = time.time() + 1

    # --- Отрисовка ---
    screen.fill(BLACK)
    draw_map(screen)
    all_sprites.draw(screen)

    # ⚡ Обновляем счёт каждый кадр
    score_text = font.render(f'{enemy_score} : {player_score}', False, (0, 255, 0))
    screen.blit(title_text, (350, 50))
    screen.blit(score_text, (380, 100))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
