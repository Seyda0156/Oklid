points = [(1, 2), (4, 6), (5, 8), (9, 10)]

def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])*2 + (point2[1] - point1[1])2)*0.5

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)
print(f"Minimum Mesafe: {min_distance}")