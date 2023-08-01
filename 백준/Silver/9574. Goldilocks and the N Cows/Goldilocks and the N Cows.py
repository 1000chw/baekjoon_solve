import sys
input = sys.stdin. readline

n, x, y, z = map(int, input().split())

temp = []
for _ in range(n):
    a, b = map(int, input().split())
    temp.append((a, 1))
    temp.append((b+1, 0))
temp.sort()
answer = 0
res = x*n
for t, s in temp:
    if s:
        res = res - x + y
        answer = max(answer, res)
    else:
        res = res - y + z

print(answer)
