import sys
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    res = 0
    p, s = input().split()
    while s in p:
        p = p.replace(s, ' ', 1)
        res += 1
    for i in p:
        if i != ' ':
            res += 1
    print(res)
