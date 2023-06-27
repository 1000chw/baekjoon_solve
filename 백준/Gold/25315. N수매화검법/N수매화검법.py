import sys
input = sys.stdin.readline

n = int(input())
weights = []
lines = []
cross = [[False]*n for _ in range(n)]

for i in range(n):
    x1, y1, x2, y2, w = map(int, input().split())
    weights.append((w, i))
    lines.append([(x1, y1), (x2, y2)])

def ccw(p1, p2, p3):
    cross_product = (p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])
    if cross_product > 0:
        return 1
    elif cross_product < 0:
        return -1
    else:
        return 0

for i in range(n-1):
    for j in range(i+1, n):
        l1_l2 = ccw(lines[i][0], lines[i][1], lines[j][0]) * ccw(lines[i][0], lines[i][1], lines[j][1])
        l2_l1 = ccw(lines[j][0], lines[j][1], lines[i][0]) * ccw(lines[j][0], lines[j][1], lines[i][1])
        cross[i][j] = (l1_l2 <= 0) and (l2_l1 <= 0)
        cross[j][i] = cross[i][j]

weights.sort()
res = 0
for w, i in weights:
    res += w*(sum(cross[i])+1)
    for j in range(n):
        if cross[i][j] == True:
            cross[j][i] = False
            cross[i][j] = False

print(res)
