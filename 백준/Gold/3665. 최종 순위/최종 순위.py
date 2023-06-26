import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    ts = [[] for _ in range(n+1)]
    for i in range(n):
        ts[t[i]] = t[i:]
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if b in ts[a]:
            ts[a].remove(b)
            ts[b].append(a)
        else:
            ts[b].remove(a)
            ts[a].append(b)
    ts.pop(0)
    if len(set(len(i) for i in ts)) == n:
        ts.sort(key=lambda x: len(x), reverse=True)
        for i in range(n-1):
            print(ts[i][0], end=" ")
        print(ts[-1][0])
    else:
        print("IMPOSSIBLE")
