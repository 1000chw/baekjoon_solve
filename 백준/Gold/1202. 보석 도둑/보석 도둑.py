import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, K = map(int, input().split())
pq = PriorityQueue()
bags = []
for _ in range(N):
    m, v = map(int, input().split())
    pq.put((m, v))

for _ in range(K):
    bags.append(int(input()))
bags.sort()
res = 0
tmp_pq = PriorityQueue()
for bag in bags:
    while pq.qsize():
        m, v = pq.get()
        if bag < m:
            pq.put((m, v))
            break
        else:
            tmp_pq.put(-v)
    if tmp_pq.qsize():
        res -= tmp_pq.get()
    elif not pq:
        break

print(res)
