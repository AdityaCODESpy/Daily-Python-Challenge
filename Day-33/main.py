# Day-33/main.py
# pip install pygame

import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PING PONG")

white = (255, 255, 255)
black = (0, 0, 0)

paddleA_y = height // 2 - 60
paddleB_y = height // 2 - 60
ball_x = width // 2
ball_y = height // 2
ball_dx = 7
ball_dy = 7

paddle_speed = 10

clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

font = pygame.font.SysFont(None, 50)

running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA_y -= paddle_speed
    if keys[pygame.K_s]:
        paddleA_y += paddle_speed
    if keys[pygame.K_UP]:
        paddleB_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddleB_y += paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y <= 0 or ball_y >= height - 20:
        ball_dy *= -1
    if ball_x <= 40 and paddleA_y <= ball_y <= paddleA_y + 120:
        ball_dx *= -1
    if ball_x >= width - 60 and paddleB_y <= ball_y <= paddleB_y + 120:
        ball_dx *= -1

    if ball_x < 0:
        scoreB += 1
        ball_x = width // 2
        ball_y = height // 2
    if ball_x > width:
        scoreA += 1
        ball_x = width // 2
        ball_y = height // 2

    # Draw
    pygame.draw.rect(screen, white, (20, paddleA_y, 20, 120))
    pygame.draw.rect(screen, white, (width - 40, paddleB_y, 20, 120))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, 20, 20))
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))

    score_text = font.render(f"{scoreA} - {scoreB}", True, white)
    screen.blit(score_text, (width // 2 - 50, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()