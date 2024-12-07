import sys
from collections import deque
input = sys.stdin.readline

cogs = [deque(), deque(), deque(), deque()]

for i in range(4):
   cogs[i].extend(list(map(int, list(input().rstrip()))))

visited = [False]*4

def rotate(ind, dd):
    visited[ind] = True
    if ind > 0 and not visited[ind-1] and cogs[ind-1][2] != cogs[ind][6]:
        rotate(ind-1, -dd)
    if ind < 3 and not visited[ind+1] and cogs[ind+1][6] != cogs[ind][2]:
        rotate(ind+1, -dd)
    cogs[ind].rotate(dd)

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    n -= 1

    rotate(n, d)
    visited = [False]*4

answer = 0

for i in range(4):
    answer += pow(2, i) * (cogs[i][0] == 1)
print(answer)

