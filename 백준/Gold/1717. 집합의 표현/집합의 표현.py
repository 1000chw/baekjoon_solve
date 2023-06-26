import sys
input = sys.stdin.readline


def findSet(node):
    if union[node] == node:
        return node
    tmp = findSet(union[node])
    union[node] = tmp
    return tmp


n, m = map(int, input().split())
union = [i for i in range(n+1)]
for _ in range(m):
    x, a, b = map(int, input().split())
    if x:
        if findSet(a) == findSet(b):
            print("YES")
        else:
            print("NO")
    else:
        union[findSet(b)] = findSet(a)
