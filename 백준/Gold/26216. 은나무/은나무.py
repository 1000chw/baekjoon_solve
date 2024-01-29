import sys

input = sys.stdin.readline
k, h, q = map(int, input().split())
x = k + 1
blueN = pow(x, h)


def solve(a, b):
    if a >= blueN or b >= blueN:
        return -1
    if a == b:
        return 0

    ta, tb = a, b
    ha, hb = h, h
    for i in range(h - 1):
        if ta % x == 0:
            ha -= 1
            ta //= x
        if tb % x == 0:
            hb -= 1
            tb //= x

    for i in range(1, h):
        tx = pow(x, i)
        if (a // tx) == (b // tx) and a % tx and b % tx:
            ha -= 1
            hb -= 1

    return ha + hb


for _ in range(q):
    a, b = map(int, input().split())
    print(solve(a, b))