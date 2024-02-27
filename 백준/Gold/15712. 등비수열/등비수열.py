import sys
from bisect import insort_left, bisect
input = sys.stdin.readline


def power(x, k, m):
    tmp = 1
    while k > 1:
        if k % 2:
            tmp *= x
            tmp %= m
        x *= x
        x %= m
        k //= 2
    return (tmp * x) % m


def solve(r, x, m):
    if x == 1:
        return 1
    mid = x // 2
    if x % 2:
        t = power(r, mid, m)
        q = solve(r, mid, m)
        return (q + t * q + t * t) % m
    else:
        t = power(r, mid, m)
        q = solve(r, mid, m)
        return (q + t * q) % m


a, r, n, mod = map(int, input().split())
print((a * solve(r, n, mod)) % mod)
