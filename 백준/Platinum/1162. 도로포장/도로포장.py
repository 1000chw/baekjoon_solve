from sys import stdin
from heapq import heappush, heappop

N,M,K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u,v,w = map(int, stdin.readline().split())
  graph[u].append((v,w))
  graph[v].append((u,w))

table = [[float('inf')]*(K+1) for _ in range(N+1)]
for i in range(K+1):
  table[1][i] = 0
heap = [(0,0,1)] # 거리, 현재까지 포장된 도로의 수, 정점번호 순
visited = [[False]*(K+1) for _ in range(N+1)]

while heap:
  dist, paved, curr = heappop(heap)
  if not visited[curr][paved]:
    visited[curr][paved] = True
    for next, weight in graph[curr]:
      if not visited[next][paved] and table[next][paved] > dist + weight:
        table[next][paved] = dist + weight
        heappush(heap, (dist+weight, paved, next))
      if paved < K:
        if not visited[next][paved+1] and table[next][paved+1] > dist:
          table[next][paved+1]= dist
          heappush(heap, (dist, paved+1, next))

print(min(table[N]))