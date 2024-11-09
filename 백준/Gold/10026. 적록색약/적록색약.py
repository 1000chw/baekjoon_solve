import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))

not_blind, blind = 0, 0
not_blind_visited, blind_visited = [[False]*n for _ in range(n)], [[False]*n for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def not_blind_dfs(cx, cy, color):
    if not not_blind_visited[cx][cy]:
        not_blind_visited[cx][cy] = True
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not not_blind_visited[nx][ny] and graph[nx][ny] == color:
                not_blind_dfs(nx, ny, color)

def blind_dfs(cx, cy, color):
    if not blind_visited[cx][cy]:
        blind_visited[cx][cy] = True
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not blind_visited[nx][ny]:
                if color == 'R' or color == 'G':
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        blind_dfs(nx, ny, color)
                elif graph[nx][ny] ==  color:
                    blind_dfs(nx, ny, color)

for i in range(n):
    for j in range(n):
        if not not_blind_visited[i][j]:
            not_blind_dfs(i, j, graph[i][j])
            not_blind += 1
        if not blind_visited[i][j]:
            blind_dfs(i, j, graph[i][j])
            blind += 1

print(not_blind, blind)
