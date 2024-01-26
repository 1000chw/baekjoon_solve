import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
par = [i for i in range(n+1)]

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def join(x, y):
    px, py = find(x), find(y)
    if px != py:
        par[px] = py

def overlap(s1, s2):
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2
    if x1 <= x4 <= x2:
        if y3 <= y1 <= y4:
            return True
        if y3 <= y2 <= y4:
            return True
    if x1 <= x3 <= x2:
        if y3 <= y2 <= y4:
            return True
        if y3 <= y1 <= y4:
            return True
    x1, y1, x2, y2 = s2
    x3, y3, x4, y4 = s1
    if x1 <= x4 <= x2:
        if y3 <= y1 <= y4:
            return True
        if y3 <= y2 <= y4:
            return True
    if x1 <= x3 <= x2:
        if y3 <= y2 <= y4:
            return True
        if y3 <= y1 <= y4:
            return True
    return False


squares = [[0, 0, 0, 0]]
for i in range(1, n+1):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    squares.append([x1, y1, x2, y2])
    for j in range(i):
        if overlap(squares[i], squares[j]):
            join(i, j)

res = -1
for i in range(n+1):
    if i == par[i]:
        res += 1

print(res)
