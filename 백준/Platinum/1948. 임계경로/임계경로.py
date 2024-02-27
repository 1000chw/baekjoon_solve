import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline


n = int(input())
m = int(input())
ch = defaultdict(list)
par = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    ch[u].append((v, w))
    par[v].append((u, w))
start, end = map(int, input().split())


def maketime(n):
    time = [0] * (n + 1)
    q = [(0, start)]
    while q:
        t, city = heappop(q)
        if time[city] == -t:
            for ncity, w in ch[city]:
                if w - t > time[ncity]:
                    time[ncity] = w - t
                    heappush(q, (t - w, ncity))
    return time


time = maketime(n)
print(time[end])

def findload():
    d = defaultdict(bool)
    q = [(time[end], end)]
    while q:
        t, city = heappop(q)
        for p, w in par[city]:
            if t - w == time[p] and not d[(p, city)]:
                d[(p, city)] = True
                heappush(q, (t-w, p))
    print(len(d.keys()))


findload()
