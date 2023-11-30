import pygame
import sys

# Function to scale a point
def scale_point(point, scale_factor):
    return (int(point[0] * scale_factor), int(point[1] * scale_factor))

# Function to scale a shape (line, triangle, square)
def scale_shape(shape, scale_factor):
    return [scale_point(point, scale_factor) for point in shape]

# Pygame initialization
pygame.init()

# Constants
width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Scaling")
clock = pygame.time.Clock()

# Line vertices
line = [(100, 100), (200, 100)]

# Triangle vertices
triangle = [(300, 100), (350, 200), (250, 200)]

# Square vertices
square = [(400, 100), (500, 100), (500, 200), (400, 200)]

# Scaling factor
scale_factor = 1.5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Draw original shapes
    pygame.draw.line(screen, black, line[0], line[1], 2)
    pygame.draw.polygon(screen, black, triangle, 2)
    pygame.draw.polygon(screen, black, square, 2)

    # Perform scaling
    scaled_line = scale_shape(line, scale_factor)
    scaled_triangle = scale_shape(triangle, scale_factor)
    scaled_square = scale_shape(square, scale_factor)

    # Draw scaled shapes
    pygame.draw.line(screen, (255,0,0), scaled_line[0], scaled_line[1], 2)
    pygame.draw.polygon(screen, (255,0,0), scaled_triangle, 2)
    pygame.draw.polygon(screen, (255,0,0), scaled_square, 2)

    pygame.display.flip()
    clock.tick(60)
