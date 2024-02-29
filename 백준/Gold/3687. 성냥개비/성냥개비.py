import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')

for _ in range(int(input())):
    n = int(input())
    big = '7' + '1' * (n // 2 - 1) if n % 2 else '1' * (n // 2)
    s = {2: 1, 3: 7, 4: 4, 5: 2, 6: 6, 7: 8, 8: 10}
    small = [[INF, INF] for _ in range(n+1)]
    if n > 6:
        s[6] = 0
    for i in range(2, min(n+1, 9)):
        small[i][0] = s[i]
        small[i][1] = 1
    if n >= 8:
        small[8][1] = 2
    for i in range(9, n+1):
        if i == n:
            s[6] = 6
        for j in range(2, 9):
            t = small[i - j][0] + pow(10, small[i - j][1]) * s[j]
            if j == 8:
                if small[i][0] > t or small[i][1] > small[i-8][1] + 2:
                    small[i][0] = t
                    small[i][1] = small[i-8][1] + 2
            elif j == 6:
                if small[i][0] > t or small[i][1] > small[i-j][1] + 1:
                    small[i][0] = t
                    small[i][1] = small[i - j][1] + 1
            else:
                if small[i][0] > t or small[i][1] > small[i-j][1] + 1:
                    small[i][0] = t
                    small[i][1] = small[i - j][1] + 1
    print(small[n][0], big)



