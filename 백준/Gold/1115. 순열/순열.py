import sys
from heapq import heappush, heappop
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
INF = float('inf')

N = int(input())
P = list(map(int, input().split()))
visited = [False]*N
ans = 0
for i in range(N):
    if not visited[i]:
        ans += 1
        x = P[i]
        while True:
            if visited[x]:
                break
            visited[x] = True
            x = P[x]
if ans == 1:
    print(0)
else:
    print(ans)
