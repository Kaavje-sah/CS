import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PACMAN_RADIUS = 20
PACMAN_COLOR = (255, 255, 0)  # Yellow
BACKGROUND_COLOR = (0, 0, 0)  # Black

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pacman Game')

# Pacman initial position and velocity
pacman_x = SCREEN_WIDTH // 2
pacman_y = SCREEN_HEIGHT // 2
pacman_velocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_RADIUS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_velocity
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_velocity
    if keys[pygame.K_UP]:
        pacman_y -= pacman_velocity
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_velocity

    pacman_x = max(PACMAN_RADIUS, min(pacman_x, SCREEN_WIDTH - PACMAN_RADIUS))
    pacman_y = max(PACMAN_RADIUS, min(pacman_y, SCREEN_HEIGHT - PACMAN_RADIUS))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
