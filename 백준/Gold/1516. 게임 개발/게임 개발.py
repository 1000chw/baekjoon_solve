import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

N = int(input())
builds = [[] for _ in range(N+1)]
times = [0]*(N+1)
res = [0]*(N+1)


def findminTime(n):
    if res[n]:
        return res[n]
    ans = 0
    for j in builds[n]:
        ans = max(ans, findminTime(j) + times[n])
    res[n] = ans
    return ans

for i in range(1, N+1):
    inform = list(map(int, input().split()))
    times[i] = inform[0]
    if inform[1] == -1:
        res[i] = times[i]
    else:
        builds[i] = inform[1:-1]

for i in range(1, N+1):
    print(findminTime(i))
