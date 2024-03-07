n = int(input())
a = list(map(int, input().split()))
aij, akl = [-float('inf')]*n, [-float('inf')]*n


m = a[0]
for i in range(1, n-2):
    if a[i] < m:
        aij[i] = max(aij[i - 1], a[i] - m)
        m = a[i]
    else:
        aij[i] = max(aij[i-1], a[i]-m)
M = a[-1]
for i in range(n-2, 1, -1):
    if a[i] > M:
        akl[i] = max(akl[i + 1], M - a[i])
        M = a[i]
    else:
        akl[i] = max(akl[i+1], M - a[i])

answer = -float('inf')
for i in range(1, n-2):
    answer = max(answer, aij[i] + akl[i+1])
print(answer)
