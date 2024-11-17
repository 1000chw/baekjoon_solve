import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

dp_min = [0]*3
dp_max = [0]*3

for i in range(n-1, -1, -1):
    graph = list(map(int, input().split()))
    max_0 = graph[0] + max(dp_max[0], dp_max[1])
    max_1 = graph[1] + max(dp_max[0], dp_max[1], dp_max[2])
    max_2 = graph[2] + max(dp_max[1], dp_max[2])
    min_0 = graph[0] + min(dp_min[0], dp_min[1])
    min_1 = graph[1] + min(dp_min[0], dp_min[1], dp_min[2])
    min_2 = graph[2] + min(dp_min[1], dp_min[2])

    dp_max = [max_0, max_1, max_2]
    dp_min = [min_0, min_1, min_2]

print(max(dp_max), min(dp_min))