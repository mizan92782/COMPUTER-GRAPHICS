import pygame
import sys

# Function to perform 2D translation of a point
def translate_point(point, translation):
    return (point[0] + translation[0], point[1] + translation[1])

# Function to perform 2D translation of a shape (line, triangle, square)
def translate_shape(shape, translation):
    return [translate_point(point, translation) for point in shape]

# Pygame initialization
pygame.init()

# Constants
width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Translation")
clock = pygame.time.Clock()

# Line vertices
line = [(100, 100), (200, 100)]

# Triangle vertices
triangle = [(300, 100), (350, 200), (250, 200)]

# Square vertices
square = [(400, 100), (500, 100), (500, 200), (400, 200)]

# Translation vector
translation_vector = (50, 50)

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

    # Perform translation
    translated_line = translate_shape(line, translation_vector)
    translated_triangle = translate_shape(triangle, translation_vector)
    translated_square = translate_shape(square, translation_vector)

    # Draw translated shapes
    pygame.draw.line(screen, (255, 0, 0), translated_line[0], translated_line[1], 2)
    pygame.draw.polygon(screen, (255, 0, 0), translated_triangle, 2)
    pygame.draw.polygon(screen, (255, 0, 0), translated_square, 2)

    pygame.display.flip()
    clock.tick(60)
