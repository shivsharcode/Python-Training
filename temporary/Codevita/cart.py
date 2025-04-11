import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        

def tcs_cart(vertices):
    x_coordinates = [vertex[0] for vertex in vertices]
    y_coordinates = [vertex[1] for vertex in vertices]

    # calculating min and max for x and y
    min_x = min(x_coordinates)
    max_x = max(x_coordinates)
    min_y = min(y_coordinates)
    max_y = max(y_coordinates)

    # calculating dimensions
    width = math.ceil(max_x - min_x)
    height = math.ceil(max_y - min_y)

    return [width, height]


n = int(input("Enter number of vertices : "))  # number of vertices
vertices = []
for _ in range(n):
    x, y = map(float, input("Enter vertex : ").split())
    vertices.append((x, y))

print(vertices)
# result
result = tcs_cart(vertices)
result.sort()
print(*result)
