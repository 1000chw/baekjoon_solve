import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
m = int(input())
students = [i for i in range(n+1)]
enemy = {i: [] for i in range(1, n+1)}
def find(x):
    if students[x] == x:
        return x
    students[x] = find(students[x])
    return students[x]

def join(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        students[py] = px

for _ in range(m):
    c, p, q = input().split()
    p, q = int(p), int(q)
    if c == 'F':
        join(p, q)
    else:
        enemy[p].append(q)

for p in enemy.keys():
    for q in enemy[p]:
        for qe in enemy[q]:
            join(p, qe)
        for pe in enemy[p]:
            join(q, pe)

res = 0
for i in range(1, n+1):
    if i == students[i]:
        res += 1
print(res)
