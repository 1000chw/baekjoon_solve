import sys
input = sys.stdin.readline

n = int(input())

max_n = [0] * (n+1)

T, P = [1] * (n+1), [0] * (n+1)

for i in range(n):
    t, p = map(int, input().split())
    T[i], P[i] = t, p

answer = 0

def solve(cur, result):
    global answer
    if cur >= n:
        answer = max(answer, result)
        return
    if cur + T[cur] > n:
        answer = max(answer, result)
    elif result < max_n[cur]:
        return
    elif result + P[cur] > max_n[cur + T[cur]]:
        max_n[cur + T[cur]] = result + P[cur]
        solve(cur + T[cur], result + P[cur])
    solve(cur + 1, result)

solve(0, 0)
print(answer)