import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(tuple(map(int, sys.stdin.readline().split())))
arr.sort()

if len(arr) != len(set(arr)):
    print(0)
    sys.exit()

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve(start, end):
    if start == end:
        return 1000000000
    mid = (start + end)//2
    min_dist = min(solve(start, mid), solve(mid + 1, end))

    points = []
    for i in range(mid, start - 1, -1):
        if (arr[i][0] - arr[mid][0])**2 < min_dist:
            points.append(arr[i])
        else:
            break
    for i in range(mid + 1, end + 1):
        if (arr[i][0] - arr[mid][0])**2 < min_dist:
            points.append(arr[i])
        else:
            break
    points.sort(key=lambda x: x[1])

    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if (points[i][1] - points[j][1])**2 < min_dist:
                min_dist = min(dist(points[i], points[j]), min_dist)
            else:
                break

    return min_dist

print(solve(0, n-1))