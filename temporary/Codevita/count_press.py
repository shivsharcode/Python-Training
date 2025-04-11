import math

def is_point_in_polygon(x, y, polygon):
    """
    Check if a point (x, y) is inside a polygon using the ray-casting algorithm.
    """
    n = len(polygon)
    inside = False
    px, py = x, y

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside

def does_block_intersect_polygon(block_x1, block_x2, block_y1, block_y2, polygon):
    """
    Check if a square block intersects with the polygon.
    """
    # Check if any corner of the block is inside the polygon
    corners = [(block_x1, block_y1), (block_x1, block_y2),
               (block_x2, block_y1), (block_x2, block_y2)]

    if any(is_point_in_polygon(x, y, polygon) for x, y in corners):
        return True

    # Check if any polygon edge intersects with the block
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        if line_intersects_rect(x1, y1, x2, y2, block_x1, block_y1, block_x2, block_y2):
            return True

    return False

def line_intersects_rect(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    """
    Check if a line segment intersects a rectangle.
    """
    # Check if either endpoint is inside the rectangle
    if (rx1 <= x1 <= rx2 and ry1 <= y1 <= ry2) or (rx1 <= x2 <= rx2 and ry1 <= y2 <= ry2):
        return True

    # Check for intersection with each rectangle edge
    if lines_intersect(x1, y1, x2, y2, rx1, ry1, rx1, ry2): return True
    if lines_intersect(x1, y1, x2, y2, rx1, ry2, rx2, ry2): return True
    if lines_intersect(x1, y1, x2, y2, rx2, ry2, rx2, ry1): return True
    if lines_intersect(x1, y1, x2, y2, rx2, ry1, rx1, ry1): return True

    return False

def lines_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Check if two line segments intersect.
    """
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    return ccw((x1, y1), (x3, y3), (x4, y4)) != ccw((x2, y2), (x3, y3), (x4, y4)) and \
           ccw((x1, y1), (x2, y2), (x3, y3)) != ccw((x1, y1), (x2, y2), (x4, y4))

def minimum_squares(n, vertices, m):
    # Step 1: Find the bounding box
    min_x = min(vertex[0] for vertex in vertices)
    max_x = max(vertex[0] for vertex in vertices)
    min_y = min(vertex[1] for vertex in vertices)
    max_y = max(vertex[1] for vertex in vertices)

    # Step 2: Define the grid dimensions
    grid_width = math.ceil((max_x - min_x) / m)
    grid_height = math.ceil((max_y - min_y) / m)

    # Step 3: Check grid cells for intersection
    covered_cells = 0
    for i in range(grid_width):
        for j in range(grid_height):
            # Define the square block
            block_x1 = min_x + i * m
            block_x2 = block_x1 + m
            block_y1 = min_y + j * m
            block_y2 = block_y1 + m

            # Check if the block intersects the polygon
            if does_block_intersect_polygon(block_x1, block_x2, block_y1, block_y2, vertices):
                covered_cells += 1

    return covered_cells

# Input from the user
n = int(input("Enter the number of vertices of the polygon: "))
vertices = [tuple(map(int, input(f"Enter vertex {i+1} (x y): ").split())) for i in range(n)]
m = int(input("Enter the side length of the square block: "))

# Calculate and print the result
result = minimum_squares(n, vertices, m)
print(f"Minimum number of square blocks required: {result}")
