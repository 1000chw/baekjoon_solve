import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
m = int(input())
v = [[[0]*n for _ in range(m+1)] for _ in range(n)]

for i in range(p[0], m+1):
    v[0][i][n-1] = i//p[0]

for i in range(1, n):
    for j in range(1, m+1):
        if j < p[i]:
            v[i][j] = v[i-1][j][:]
            continue
        before = v[i-1][j][:]
        after = v[i][j-p[i]][:]
        after[n-1-i] += 1
        after2 = v[i-1][j-p[i]][:]
        after2[n - 1 - i] += 1
        after3 = v[0][j-p[i]][:]
        after3[n - 1 - i] += 1
        ml = []
        if sum(before) != before[n-1] and sum(before) > sum(after3):
            ml = before
        else:
            ml = after3
        if sum(ml) <= sum(after2):
            ml = after2
        if sum(ml) <= sum(after):
            ml = after
        v[i][j] = ml


if sum(v[n-1][m]) == v[n-1][m][n-1]:
    print(0)
else:
    for i in range(n):
        for j in range(v[n-1][m][i]):
            print(n-1-i, end='')
