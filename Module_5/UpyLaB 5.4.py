def distance_points(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


print(distance_points((1.0, 1.0), (2.0, 1.0)))   # 1.0
print(distance_points((-1.0, 0.5), (2.0, 1.0)))  # 3.0413812651491097
