import sys
input = sys.stdin.readline
INF = float('inf')

depth = [0]*40001
water = [INF]*40001
bx = 0
n = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    n = x
    if i:
        if i % 2:
            bx = x
        else:
            for j in range(bx, x):
                depth[j] = y

for _ in range(int(input())):
    x, y, z, w = map(int, input().split())
    min_d = depth[x]
    for i in range(x-1, -1, -1):
        min_d = min(min_d, depth[i])
        water[i] = min(water[i], depth[i] - min_d)
    min_d = depth[x]
    for i in range(x, n):
        min_d = min(min_d, depth[i])
        water[i] = min(water[i], depth[i] - min_d)

print(sum(water[:n]))