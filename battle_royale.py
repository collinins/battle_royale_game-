import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Battle Royale Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size * 2]
player_speed = 10

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

# Clock to control game speed
clock = pygame.time.Clock()

# Function to detect collision between player and enemy
def detect_collision(player_pos, enemy_pos):
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    return player_rect.colliderect(enemy_rect)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    # Update enemy position
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] >= HEIGHT:
        # Reset the enemy to the top with a random horizontal position
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    # Collision detection
    if detect_collision(player_pos, enemy_pos):
        print("Collision detected! Game Over")
        running = False

    # Draw player and enemy
    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Update display
    pygame.display.update()

    # Control frame rate
    clock.tick(30)

pygame.quit()
