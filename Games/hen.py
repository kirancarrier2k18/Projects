import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hen Face")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Draw hen face
def draw_hen_face():
    screen.fill(WHITE)

    # Face
    pygame.draw.circle(screen, YELLOW, (300, 300), 150)

    # Eyes
    pygame.draw.circle(screen, WHITE, (250, 250), 30)
    pygame.draw.circle(screen, WHITE, (350, 250), 30)
    pygame.draw.circle(screen, BLACK, (250, 250), 10)
    pygame.draw.circle(screen, BLACK, (350, 250), 10)

    # Beak
    pygame.draw.polygon(screen, ORANGE, [(300, 300), (270, 360), (330, 360)])

    # Comb (top red part)
    pygame.draw.circle(screen, RED, (270, 150), 25)
    pygame.draw.circle(screen, RED, (300, 140), 25)
    pygame.draw.circle(screen, RED, (330, 150), 25)

    # Wattle (bottom red part)
    pygame.draw.circle(screen, RED, (280, 390), 20)
    pygame.draw.circle(screen, RED, (320, 390), 20)

    pygame.display.flip()

# Main loop
running = True
while running:
    draw_hen_face()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
