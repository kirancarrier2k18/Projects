import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 20
GRID_WIDTH = 40
GRID_HEIGHT = 30
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Long Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 24)

def draw_cell(position, color):
    x, y = position
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def random_position(exclude):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in exclude:
            return pos

def main():
    snake = [(20 - i, 15) for i in range(15)]  # Start with a long snake
    direction = RIGHT
    food = random_position(snake)
    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (head in snake or
                head[0] < 0 or head[0] >= GRID_WIDTH or
                head[1] < 0 or head[1] >= GRID_HEIGHT):
            print("Game Over! Final Score:", score)
            running = False
            continue

        else:
            snake.pop()

        for segment in snake:
            draw_cell(segment, GREEN)
        draw_cell(food, RED)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

main()
