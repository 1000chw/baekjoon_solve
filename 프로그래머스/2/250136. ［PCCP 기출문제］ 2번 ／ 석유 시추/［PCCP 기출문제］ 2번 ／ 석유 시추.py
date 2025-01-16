from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
def solution(land):
    answer = 0
    oils = defaultdict(set)
    num = 0
    cols = [0] * len(land[0])
    visited = [[False]*len(land[0]) for _ in range(len(land))]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
    def dfs(i, j):
        if visited[i][j]:
            return 0
        visited[i][j] = True
        oils[num] |= {j}
        cnt = 1
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and not visited[nx][ny] and land[nx][ny]:
                cnt += dfs(nx, ny)
                
        return cnt
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] and not visited[i][j]:
                cnt = dfs(i, j)
                for col in list(oils[num]):
                    cols[col] += cnt
                num += 1
    return max(cols)