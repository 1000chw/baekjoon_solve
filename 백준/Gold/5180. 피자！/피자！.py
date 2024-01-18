import sys
from math import pi, sqrt
input = sys.stdin.readline

for i in range(1, int(input())+1):
    result = 1
    n = int(input())
    points = []

    for j in range(n):
        a, r = map(float, input().split())
        points.append(a)
    points_l = [list(sorted(map(lambda x: (x - points[j] + 2*pi) % (2 * pi), points))) for j in range(n)]
    for j in range(2, n+1):
        for point in points_l:
            if n % j == 0:
                start = 0
                slice_a = 2 * pi / j
                nuggets = n // j
                cnt = 0
                chk = False
                for p in point:
                    if p < start + slice_a:
                        cnt += 1
                    else:
                        if cnt != nuggets:
                            chk = True
                            break
                        cnt = 0
                        start += slice_a
                        if p < start + slice_a:
                            cnt += 1
                        else:
                            chk = True
                            break
                if cnt != nuggets:
                    chk = True
                if chk:
                    continue
                if 2*pi - slice_a <= point[-1]:
                    result = j
                    break

    print(f'Data Set {i}: {result} slices\n')
