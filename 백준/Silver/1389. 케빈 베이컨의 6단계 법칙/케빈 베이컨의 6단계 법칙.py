import sys
from queue import Queue
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
res = [0]*N
for i in range(1, N+1):
    visited = [False] * (N + 1)
    que = Queue()
    que.put((i, 0))
    while que.qsize():
        x, cnt = que.get()
        if visited[x]:
           continue
        res[i-1] += cnt
        visited[x] = True
        for k in graph[x]:
            if not visited[k]:
                que.put((k, cnt+1))
print(res.index(min(res))+1)
