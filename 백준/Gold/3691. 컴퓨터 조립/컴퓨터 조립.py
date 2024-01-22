import sys
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')

for _ in range(int(input())):
    n, b = map(int, input().split())
    parts = defaultdict(list)
    left, right = INF, 0
    for _ in range(n):
        type, name, p, q = input().split()
        parts[type].append((int(p), int(q)))
        left = min(left, int(q))
        right = max(right, int(q))
    res = 0
    while left < right:
        mid = (left + right) // 2
        cost = 0
        quality = INF
        for part in parts.keys():
            min_c, min_q = INF,  0
            for p, q in parts[part]:
                if q >= mid and min_c > p:
                    min_c, min_q = p, q
            if min_c == INF:
                cost = INF
                break
            cost += min_c
            quality = min(quality, min_q)
        if cost > b:
            right = mid - 1
        else:
            res = quality
            left = mid + 1
    print(res)