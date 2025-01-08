import sys
input = sys.stdin.readline

n = int(input())

par = list(map(int, input().split()))
tree = [[] for _ in range(n)]

for i in range(1, n):
    tree[par[i]].append(i)

def dfs(node):
    ds = []
    for n in tree[node]:
        ds.append(dfs(n))
    ds.sort(reverse=True)
    for i in range(len(ds)):
        ds[i] += i + 1
    if ds:
        return max(ds)
    return 0

print(dfs(0))
