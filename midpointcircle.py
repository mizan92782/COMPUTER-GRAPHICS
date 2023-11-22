import matplotlib.pyplot as plt

def draw_circle(radius):
    x = radius
    y = 0
    p = 1 - radius  

    x_points = []
    y_points = []

    plot_points(x, y, x_points, y_points)

    while x > y:
        y += 1

        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

        if x < y:
            break

        plot_points(x, y, x_points, y_points)
        plot_points(y, x, x_points, y_points)
        plot_points(-x, y, x_points, y_points)
        plot_points(-y, x, x_points, y_points)
        plot_points(-x, -y, x_points, y_points)
        plot_points(-y, -x, x_points, y_points)
        plot_points(x, -y, x_points, y_points)
        plot_points(y, -x, x_points, y_points)

    # Display the circle using matplotlib
    plt.scatter(x_points, y_points)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def plot_points(x, y, x_points, y_points):
    x_points.append(x)
    y_points.append(y)

# Example: Draw a full circle with radius 5
draw_circle(300)
