import sys
from collections import defaultdict
from queue import Queue
input = sys.stdin.readline

n, m = map(int, input().split())
ls = defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    ls[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    ls[x] = y

queue = Queue()
visited = [False] * 101
queue.put((1, 0))

while not queue.empty():
    x, cnt = queue.get()
    if x == 100:
        print(cnt)
        break

    if visited[x]: continue
    visited[x] = True
    for i in range(1, 7):
        nx = x + i
        if ls[nx]:
            nx = ls[nx]
        if nx <= 100 and not visited[nx]:
            queue.put((nx, cnt + 1))
