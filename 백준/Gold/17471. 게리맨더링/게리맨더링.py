import sys
from itertools import combinations
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(c, cur, visited):
    answer = people[cur]
    visited[cur] = True
    for next_ in graph[cur]:
        if next_ in c and not visited[next_]:
            answer += dfs(c, next_, visited)

    return answer

def dfs1(c, cur, visited):
    answer = people[cur]
    visited[cur] = True
    for next_ in graph[cur]:
        if next_ not in c and not visited[next_]:
            answer += dfs1(c, next_, visited)

    return answer

n = int(input())
people = [0] + list(map(int, input().split()))

graph = {}
for i in range(1, n+1):
    x = list(map(int, input().split()))
    graph[i] = x[1:]
result = -1
for i in range(1, n//2+1):
    cs = combinations(range(1, n+1), i)

    for c in cs:
        visited = [False] * (n+1)
        a1 = dfs(c, c[0], visited)
        chk = False
        for k in c:
            if not visited[k]:
                chk = True
                break
        if chk:
            continue
        a2 = 0
        for j in range(1, n+1):
            if j not in c:
                a2 = dfs1(c, j, visited)
                break
        if all(visited[1:]):

            if result == -1:
                result = abs(a1 - a2)
            else:
                result = min(result, abs(a1 - a2))
print(result)
