import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
MOD = 1000000007

N, M = map(int, input().split())
li = [i for i in range(N+1)]

def pow2(n):
    res = 2
    for _ in range(n - 1):
        res *= 2
        res %= MOD
    return res

def find(n):
    if li[n] == n:
        return n
    else:
        li[n] = find(li[n])
        return li[n]

for _ in range(M):
    l, r, k = map(int, input().split())
    for i in range(l, l + k):
        for j in range(1, (r - i) // k + 1):
            if li[i + j*k] == 0:
                li[i + j*k] = i
            else:
                x = find(li[i + j*k])
                y = find(i)
                if x != y:
                    li[y] = li[x]
s = 0
for i in range(1, N+1):
    if li[i] == i:
        s += 1
print(pow2(s))
