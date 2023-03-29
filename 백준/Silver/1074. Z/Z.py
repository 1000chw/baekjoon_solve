import math
import sys

N, r, c = map(int, sys.stdin.readline().split())
N = int(math.pow(2, N))
num = 0
x = 0
y = 0

while N != 1:
    N //= 2
    tmp = N * N
    if r < x + N and c < y + N:
        continue
    elif r < x + N:
        num += tmp
        y += N
    elif c < y + N:
        num += tmp * 2
        x += N
    else:
        num += tmp * 3
        x += N
        y += N

print(num)
