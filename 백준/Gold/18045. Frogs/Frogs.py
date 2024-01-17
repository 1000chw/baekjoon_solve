import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    stones = [[[], []] for _ in range(n)]
    for i in range(n):
        r, s = map(int, input().split())
        left = i - r if i - r >= 0 else 0
        stones[left][0].append(-s)
        if i + r < n:
            stones[i + r][1].append(-s)
    res = 0
    q = []
    for i in range(n):
        for x in stones[i][0]:
            heapq.heappush(q, x)
        if len(q) >= 3 and stones[i][0]:
            res = max(res, -sum(heapq.nsmallest(3, q)))
        for x in stones[i][1]:
            q.remove(x)
    print(res)
