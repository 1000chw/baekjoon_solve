from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N = int(input())
tree = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visited = [False for _ in range(N+1)]
visited[1] = True
answer = 0
stack = deque()
for i in tree.keys():
    if i != 1 and len(tree[i]) == 1:
        tree[i] = []

stack.append((0, 1))
while stack:
    depth, n = stack.pop()
    if not tree[n]:
        answer += depth
        continue
    for i in tree[n]:
        if not visited[i]:
            visited[i] = True
            stack.append((depth+1, i))

if answer % 2:
    print("Yes")
else:
    print("No")