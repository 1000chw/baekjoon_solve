import sys
input = sys.stdin.readline

def solve(n):
    answer = 0

    mod = 1
    while True:
        x, y, z = n // (mod * 10), n % mod + 1, (n % (mod * 10)) // mod
        if not x:
            answer += y * z + (z * (z - 1) * mod) // 2
            return answer
        answer += 45 * x * mod + y * z + (z * (z - 1) * mod) // 2 if z else 45 * x * mod
        mod *= 10


for _ in range(int(input())):
    n, m = map(int, input().split())
    if not n:
        n = 1
    print(solve(m) - solve(n-1))

