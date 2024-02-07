import sys
input = sys.stdin.readline

N, M = map(int, input().split())
kingdoms = {}

def find(k):
    if kingdoms[k] == k:
        return k
    kingdoms[k] = find(kingdoms[k])
    return kingdoms[k]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        kingdoms[px] = py
    else:
        kingdoms[y] = y
        kingdoms[px] = y

for _ in range(N):
    kingdom = input().strip()
    kingdoms[kingdom] = kingdom

for _ in range(M):
    x, y, n = input().strip().split(',')
    if n == '1':
        x, y = y, x
    union(x, y)
res = [key for key in kingdoms.keys() if key == kingdoms[key]]
print(len(res))
res.sort()
for r in res:
    print(r)
