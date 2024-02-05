from math import sqrt
INF = float('inf')

T = [[0]*5 for _ in range(1001)]

def solve(n, r):
    if n == 1:
        return 1
    if T[n][r]:
        return T[n][r]
    if r == 3:
        T[n][r] = solve(n-1, r) * 2 + 1
        return T[n][r]
    k = n - int(round(sqrt(2*n + 1))) + 1
    T[n][r] = 2 * solve(k, r) + solve(n - k, r - 1)
    return T[n][r]


cnt = 1
while True:
    try:
        x = input()
        print(f"Case {cnt}: {solve(int(x), 4)}")
        cnt += 1
    except:
        break
