import sys
input = sys.stdin.readline
INF = float('inf')
N = int(input())
mm, Mm, mp, Mp = INF, -INF, INF, -INF
for i in range(N):
    x, y = map(int, input().split())
    mm = min(mm, x - y)
    Mm = max(Mm, x - y)
    mp = min(mp, x + y)
    Mp = max(Mp, x + y)

print(max(Mm - mm, Mp - mp))