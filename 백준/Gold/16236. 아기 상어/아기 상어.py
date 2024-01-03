import sys
from collections import defaultdict
from queue import Queue
input = sys.stdin.readline

n = int(input())
fishes = []
fish_count = [0, 0, 0, 0, 0, 0, 0]
visited = [[False]*n for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cur = [0, 0]
size = 2
count = 0
time = 0

for i in range(n):
    line = list(map(int, input().split()))
    fishes.append(line)
    for j in range(n):
        if line[j] == 9:
            cur = [i, j]
        elif line[j]:
            fish_count[line[j]] += 1

fishes[cur[0]][cur[1]] = 0

while sum(fish_count[1:size if size < 7 else 7]):
    visited = [[False]*n for _ in range(n)]
    candidates = []
    ct = -1
    q = Queue()
    q.put(cur+[0])
    while q.qsize():
        x, y, t = q.get()
        if ct != -1 and t > ct:
            break
        if visited[x][y]:
            continue
        visited[x][y] = True
        if 0 < fishes[x][y] < size:
            ct = t
            candidates.append([x, y])
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if fishes[nx][ny] > size:
                    visited[nx][ny] = True
                else:
                    q.put([nx, ny, t+1])
    candidates.sort()
    if not candidates:
        break
    fx, fy = candidates[0]
    fish_count[fishes[fx][fy]] -= 1
    time += ct
    fishes[fx][fy] = 0
    cur = [fx, fy]
    count += 1
    if count == size:
        count = 0
        size += 1

print(time)
