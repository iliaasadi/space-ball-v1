# Import Libs
import pygame
import sys

pygame.init()

# Game's Icon
ICON = pygame.image.load('Space_Ball_v1_icon.png')

# Set Icon
pygame.display.set_icon(ICON)

# Width & Height of Screen
WIDTH, HEIGHT = 1530, 795

# Player_Color
COLOR = (255, 204, 0)

# Ball Size
BALL_SIZE = 20

# PLayer Size & Speed
PLAYER_SIZE = 50
PLAYER_SPEED = 5.5

# Ball Speed X/Y
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Ball")

ball_image = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)
pygame.draw.circle(ball_image, (255, 0, 0), (BALL_SIZE // 2, BALL_SIZE // 2), BALL_SIZE // 2)
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_image.fill(COLOR)

# Player
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - 2 * PLAYER_SIZE

# Ball
ball_x = WIDTH // 6 - BALL_SIZE // 6
ball_y = HEIGHT // 6 - BALL_SIZE // 6
ball_x_speed = BALL_SPEED_X
ball_y_speed = BALL_SPEED_Y

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    if ball_x <= 0 or ball_x >= WIDTH - BALL_SIZE:
        ball_x_speed = -ball_x_speed

    if ball_y <= 0:
        ball_y_speed = -ball_y_speed

    if (
        player_x < ball_x + BALL_SIZE
        and player_x + PLAYER_SIZE > ball_x
        and player_y < ball_y + BALL_SIZE
        and player_y + PLAYER_SIZE > ball_y
    ):
        ball_y_speed = -ball_y_speed

    if ball_y >= HEIGHT:
        running = False

    window.fill((0, 0, 0))
    window.blit(player_image, (player_x, player_y))
    window.blit(ball_image, (ball_x, ball_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
