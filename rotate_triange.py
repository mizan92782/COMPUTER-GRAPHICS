import pygame
import sys
import math

# Function to rotate a point (x, y) around the origin (0, 0)
def rotate_point(x, y, angle):
    radians = math.radians(angle)
    x_rotated = x * math.cos(radians) - y * math.sin(radians)
    y_rotated = x * math.sin(radians) + y * math.cos(radians)
    return x_rotated, y_rotated

# Function to rotate a point (x, y) around a fixed point (center_x, center_y)
def rotate_point_around_fixed(x, y, center_x, center_y, angle):
    x_relative = x - center_x
    y_relative = y - center_y
    x_rotated, y_rotated = rotate_point(x_relative, y_relative, angle)
    return x_rotated + center_x, y_rotated + center_y

# Pygame initialization
pygame.init()

# Constants
width, height = 800, 600
origin = (width // 2, height // 2)
fixed_point = (width // 6, height // 6)
triangle_size = 50

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triangle Rotation")
clock = pygame.time.Clock()

# Triangle vertices
triangle_vertices = [
    (origin[0], origin[1] - triangle_size),
    (origin[0] - triangle_size / 2, origin[1] + triangle_size / 2),
    (origin[0] + triangle_size / 2, origin[1] + triangle_size / 2)
]

# Main loop
angle = 0
fixed_rotation_angle = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    # Rotate triangle around the origin
    rotated_triangle = [
        rotate_point(vertex[0], vertex[1], angle) for vertex in triangle_vertices
    ]

    # Rotate triangle around the fixed point
    rotated_triangle_fixed = [
        rotate_point_around_fixed(vertex[0], vertex[1], fixed_point[0], fixed_point[1], fixed_rotation_angle)
        for vertex in rotated_triangle
    ]

    # Draw triangles
    pygame.draw.polygon(screen, black, rotated_triangle, 2)
    pygame.draw.polygon(screen, black, rotated_triangle_fixed, 4)

    pygame.display.flip()
    clock.tick(60)

    # Increment the rotation angle
    angle += 1
    if angle == 360:
        angle = 0

    pygame.time.delay(20)  # Add a slight delay to make the rotation visible
