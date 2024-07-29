points = [(2, 5), (5, 6), (4, 9), (6, 3)]
def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**(1/2)
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        print(f"{points[i]}, {points[j]} : {dist}")

if distances:
    min_distance = min(distances)
    print("minimum mesafe:", min_distance)
else:
    print("Hesaplanacak mesafe bulunamadı.")