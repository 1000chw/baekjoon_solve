import sys
from math import log2
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
H = int(log2(n))+1

tree = [[] for _ in range(n+1)]
parent = [[0]*(H+1) for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def makeParents(node, par, dep):
    parent[node][0] = par
    depth[node] = dep

    for next_ in tree[node]:
        if next_ != par:
            makeParents(next_, node, dep+1)

def findLCA(a, b):
    if depth[a] != depth[b]:
        if depth[a] < depth[b]:
            a, b = b, a

        dif = depth[a] - depth[b]
        ind = 0
        while dif > 0:
            if dif % 2:
                a = parent[a][ind]
            dif = dif >> 1
            ind += 1
    if a == b:
        return a

    for i in range(H-1, -1, -1):
        if parent[a][i] and parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

makeParents(1, 0, 0)

for i in range(1, H):
    for j in range(1, n+1):
        if parent[j][i-1]:
            parent[j][i] = parent[parent[j][i-1]][i-1]



for _ in range(int(input())):
    a, b = map(int, input().split())
    print(findLCA(a, b))
