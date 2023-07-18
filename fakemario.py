import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Game")

# Define colors
WHITE = (255, 255, 255)

# Define player properties
player_width, player_height = 40, 60
player_x = 50
player_y = screen_height - player_height - 10
player_y_velocity = 0
gravity = 1

# Define ground properties
ground_height = 40

# Define enemy properties
enemy_width, enemy_height = 40, 40
enemy_x = screen_width
enemy_y = screen_height - enemy_height - ground_height - 10
enemy_x_velocity = -5

# Load images
player_img = pygame.image.load("D:/Newfolder/WebJ/mario.png")
player_img = pygame.transform.scale(player_img, (player_width, player_height))
enemy_img = pygame.image.load("D:/Newfolder/WebJ/enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_y_velocity = -15

    # Update player
    player_y_velocity += gravity
    player_y += player_y_velocity

    # Check collision with ground
    if player_y > screen_height - player_height - ground_height:
        player_y = screen_height - player_height - ground_height
        player_y_velocity = 0

    # Update enemy
    enemy_x += enemy_x_velocity

    # Check collision with enemy
    if player_x + player_width > enemy_x and \
       player_x < enemy_x + enemy_width and \
       player_y + player_height > enemy_y:
        running = False

    # Check if enemy is off-screen
    if enemy_x < -enemy_width:
        enemy_x = screen_width
        enemy_y = random.randint(screen_height - enemy_height - ground_height - 50, screen_height - enemy_height - ground_height)

    # Draw background
    screen.fill(WHITE)

    # Draw ground
    pygame.draw.rect(screen, (0, 255, 0), (0, screen_height - ground_height, screen_width, ground_height))

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw enemy
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Update the game display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
