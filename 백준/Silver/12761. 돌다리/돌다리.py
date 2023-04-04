import sys
from queue import Queue
input = sys.stdin.readline

A, B, N, M = map(int, input().split())
dx = [1, -1, A, -A, B, -B]
visited = [False]*100001
visited[N] = True
que = Queue()
que.put((N, 0))

while not que.empty():
    x, cnt = que.get()
    if x == M:
        print(cnt)
        break
    if 0 < x * A < 100001 and not visited[x * A]:
        que.put((x * A, cnt + 1))
        visited[x * A] = True
    if 0 < x * B < 100001 and not visited[x * B]:
        que.put((x * B, cnt + 1))
        visited[x * B] = True
    for i in dx:
        nx = x + i
        if 0 <= nx < 100001 and not visited[nx]:
            que.put((nx, cnt + 1))
            visited[nx] = True
