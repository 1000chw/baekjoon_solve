import sys
input = sys.stdin.readline

N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    node[x].append(y)
    node[y].append(x)
answer = 0
for i in range(1, N+1):
    if not visited[i]:
        answer += 1
        stack = [i]
        while len(stack):
            x = stack.pop()
            if visited[x]:
                continue
            visited[x] = True
            for nx in node[x]:
                if not visited[nx]:
                    stack.append(nx)
print(answer)
