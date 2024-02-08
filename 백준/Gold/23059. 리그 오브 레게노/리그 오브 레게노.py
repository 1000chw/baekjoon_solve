import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
items = defaultdict(list)
link = defaultdict(int)
pq = []

for _ in range(n):
    x, y = input().split()
    items[x].append(y)
    link[y] += 1
    link[x] += 0
for key in link.keys():
    if not link[key]:
        heappush(pq, key)

if not pq:
    print(-1)
else:
    res = []
    while pq:
        next_items = []
        while pq:
            item = heappop(pq)
            res.append(item)
            for next_item in items[item]:
                link[next_item] -= 1
                if not link[next_item]:
                    heappush(next_items, next_item)
        pq = next_items

    if len(link.keys()) == len(res):
        for item in res:
            print(item)
    else:
        print(-1)
