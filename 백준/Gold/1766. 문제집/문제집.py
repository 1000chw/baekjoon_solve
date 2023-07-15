from sys import stdin
from queue import PriorityQueue
input = stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]
parent = {i: 0 for i in range(1,N+1)}
q = PriorityQueue()
for _ in range(M):
    x, y = map(int, input().split())
    tree[x].append(y)
    parent[y] += 1

for i in range(1, N+1):
    if not parent[i]:
        q.put(i)

while q.qsize():
    node = q.get()
    for i in tree[node]:
        parent[i] -= 1
        if not parent[i]:
            q.put(i)
    print(node, end=' ')
