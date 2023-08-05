import sys
input = sys.stdin. readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()
max_n = (x[-1] - x[0]) // (c - 1)
c -= 1

l, r, m = 1, max_n, 0
while l < r:
    last = 0
    m = (l + r)//2 + 1
    cnt = 0
    cnt1 = 0
    for i in range(1, n):
        if x[i] - x[last] >= m:
            if x[i] - x[last] == m:
                cnt1 += 1
            cnt += 1
            last = i
    if cnt >= c:
        if cnt1 == 0:
            l = m + 1
        else:
            l = m
    else:
        r = m-1
print(l)
