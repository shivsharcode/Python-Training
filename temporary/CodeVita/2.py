import math

node_coords = {1: (0, 0)}


def calculate_distance(dev_id1, dev_id2):
    x1, y1 = node_coords[dev_id1]
    x2, y2 = node_coords[dev_id2]

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def polar_to_cartesian(origin, distance, angle):
    # converting angles to radians
    angle_rad = math.radians(angle)
    x = origin[0] + distance * math.cos(angle_rad)
    y = origin[1] + distance * math.sin(angle_rad)
    return (x, y)


# func to calculate coordinates
def calculate_coordinates(data):
    for node, connections in data.items():
        if node not in node_coords:
            continue

        origin = node_coords[node]
        for connected_node, distance, angle in connections:
            if connected_node not in node_coords:
                # calculating position of the connected node
                coord = polar_to_cartesian(origin, distance, angle)
                node_coords[connected_node] = coord

    return node_coords


n = int(input())  # no. of placefinder devices

li = input().split()
it = 0
data = {}
for _ in range(n):
    devID = int(input())
    colonIdx = li[it].index(':')
    numberOfDevConnected = int(li[it][colonIdx + 1:])

    devInfo = []
    for _ in range(numberOfDevConnected):
        s = input().split()
        connected_node = int(s[0])
        distance = float(s[1])
        angle = float(s[2])
        devInfo.append([connected_node, distance, angle])

    data[devID] = devInfo

    it += 1
# last line of input
concernedDevIds = list(map(int, input().split()))

coordinates = calculate_coordinates(data)
dev_id1, dev_id2 = concernedDevIds
distance = calculate_distance(dev_id1, dev_id2)
distance = round(distance, 2)
print(distance, end="")