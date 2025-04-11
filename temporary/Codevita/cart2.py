import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def rotate_point(point, angle):
    return Point(
        point.x * math.cos(angle) - point.y * math.sin(angle),
        point.x * math.sin(angle) + point.y * math.cos(angle)
    )

def calculate_bounding_box(vertices, angle):
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')

    for vertex in vertices:
        rotated_vertex = rotate_point(vertex, angle)
        min_x = min(min_x, rotated_vertex.x)
        max_x = max(max_x, rotated_vertex.x)
        min_y = min(min_y, rotated_vertex.y)
        max_y = max(max_y, rotated_vertex.y)

    return max_x - min_x, max_y - min_y






num_vertices = int(input("Enter the number of vertices: "))
vertices = []

for _ in range(num_vertices):
    x_coordinate, y_coordinate = map(float, input().split())
    vertices.append(Point(x_coordinate, y_coordinate))

minimum_area = float('inf')
optimal_width, optimal_height = 0, 0

for degree in range(360):
    angle_in_radians = degree * math.pi / 180.0
    width, height = calculate_bounding_box(vertices, angle_in_radians)
    area = width * height

    if area < minimum_area:
        minimum_area = area
        optimal_width = width
        optimal_height = height

if optimal_width > optimal_height:
    optimal_width, optimal_height = optimal_height, optimal_width

print(f"{math.ceil(optimal_width)} {math.ceil(optimal_height)}", end="")




