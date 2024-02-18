import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
X = []
totalP = 0
for _ in range(N):
    X.append(tuple(map(int, input().split())))
    totalP += X[-1][1]

X.sort()
MM1 = 0
sum_p1 = 0
for i in range(N):
    if i:
        sum_p1 += i*(X[i][0] - X[i-1][0])
    if i != N-1:
        MM1 = max(MM1, X[N-1][0] - X[i][0] + X[i][1])
    else:
        MM1 = max(MM1, i*(X[i][0] - X[i-1][0]) + X[i][1])
MM2 = 0
sum_p2 = 0
for i in range(N-1, -1, -1):
    if i != N-1:
        sum_p2 += (N-1-i)*(X[i+1][0] - X[i][0])
    if i != 0:
        MM2 = max(MM2, X[i][0] - X[0][0] + X[i][1])
    else:
        MM2 = max(MM2, (N-1-i)*(X[i+1][0] - X[i][0]) + X[i][1])

print(min(totalP + sum_p1 - MM1, totalP + sum_p2 - MM2))


