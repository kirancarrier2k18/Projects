import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 8000, 6000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dragon Animation")

# Constants
N = 100  # Number of segments
rad = 0.1
segments = [{'x': width // 9, 'y': height // 9} for _ in range(N)]
pointer = {'x': width // 2, 'y': height // 2}
clock = pygame.time.Clock()

# Colors
HEAD_COLOR = (2, 0, 100)
BODY_COLOR = (0, 255, 0)
EYE_COLOR = (255, 255, 255)

def run(frm):
    global segments

    # Oscillating motion
    ax = (math.cos(9 * frm) * rad * width) / height
    ay = (math.sin(4 * frm) * rad * height) / width

    # Head follows pointer with oscillation
    head = segments[0]
    head['x'] += (ax + pointer['x'] - head['x']) / 10
    head['y'] += (ay + pointer['y'] - head['y']) / 10

    # Body segments follow the previous one
    for i in range(1, N):
        curr = segments[i]
        prev = segments[i - 1]
        angle = math.atan2(curr['y'] - prev['y'], curr['x'] - prev['x'])

        curr['x'] += (prev['x'] - curr['x'] + math.cos(angle) * (100 - i) / 5) / 4
        curr['y'] += (prev['y'] - curr['y'] + math.sin(angle) * (100 - i) / 5) / 4

def draw():
    screen.fill((0, 0, 0))

    # Draw body segments
    for i in range(N - 1, 0, -1):
        pygame.draw.circle(screen, BODY_COLOR, (int(segments[i]['x']), int(segments[i]['y'])), max(4, 10 - i // 3))

    # Draw head
    head = segments[0]
    pygame.draw.circle(screen, HEAD_COLOR, (int(head['x']), int(head['y'])), 12)

    # Draw eyes
    eye_offset = 5
    pygame.draw.circle(screen, EYE_COLOR, (int(head['x'] + eye_offset), int(head['y'] - eye_offset)), 3)
    pygame.draw.circle(screen, EYE_COLOR, (int(head['x'] - eye_offset), int(head['y'] - eye_offset)), 3)

    pygame.display.flip()

# Main loop
frm = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pointer['x'], pointer['y'] = pygame.mouse.get_pos()
    run(frm)
    draw()
    frm += 0.01
    clock.tick(60)
