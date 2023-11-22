import matplotlib.pyplot as plt

def translate_point(point, delta_x, delta_y):
    """Translate a 2D point by (delta_x, delta_y)."""
    x, y = point
    translated_point = (x + delta_x, y + delta_y)
    return translated_point

def translate_shape(shape, delta_x, delta_y):
    """Translate a list of 2D points representing a shape by (delta_x, delta_y)."""
    new_translated_shape = [translate_point(point, delta_x, delta_y) for point in shape]
    return new_translated_shape

def plot_shape(shape, label, color):
    """Plot a shape on the graph."""
    x, y = zip(*shape + [shape[0]])  # Closing the shape by repeating the first point
    plt.plot(x, y, label=label, color=color)











# Original square
original_square = [(0, 0), (1, 0), (1, 1), (0, 1)]

# Translation values
delta_x = 2
delta_y = 3

# Translate the square
translated_square = translate_shape(original_square, delta_x, delta_y)

# Plot the original and translated squares
plot_shape(original_square, 'Original Square', 'blue')
plot_shape(translated_square, 'Translated Square', 'red')

# Set axis limits
plt.xlim(-1, 4)
plt.ylim(-1, 5)

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Translation in Computer Graphics')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
