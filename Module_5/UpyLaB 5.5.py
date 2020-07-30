def distance_points(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def longueur(*points):
    longer = 0
    for i in range(len(points) - 1):
        longer += distance_points(points[i], points[i + 1])
    return longer


print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))  # 2.0
print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))  # 7.1122677042334645
