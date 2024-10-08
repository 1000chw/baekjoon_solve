MOD = 1000000007

def factorial(N):
    result = 1
    for i in range(2, N + 1):
        result *= i
    return result

k, n = map(int, input().split())
res = 1

for i in range(k+1):
    res = (res * (k + n - i)) % MOD

res = res * pow(factorial(k+1), MOD-2, MOD) % MOD

print(res)
