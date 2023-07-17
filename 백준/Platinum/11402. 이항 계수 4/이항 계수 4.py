import sys
sys.setrecursionlimit(100000000)
n, k, m = map(int, input().split())


def get_luka(N, M):
    li = []
    while N > 0:
        li.append(N % M)
        N //= M
    return li

li = [[-1]*2001 for _ in range(2001)]

def comb(N, K):
    if N < K:
        return 0
    if N / 2 < K:
        K = N - K
    x = li[N][K]
    if x != -1:
        return x
    if K == 0:
        return 1
    if K == 1:
        li[N][K] = N
        return N
    li[N][K] = (comb(N - 1, K - 1) + comb(N - 1, K)) % m
    return li[N][K]

luka_n = get_luka(n, m)
luka_k = get_luka(k, m)

min_idx = min(len(luka_n), len(luka_k))
res = 1
for i in range(min_idx):
    res *= comb(luka_n[i], luka_k[i])
    res %= m
    if not res:
        break

print(res)

