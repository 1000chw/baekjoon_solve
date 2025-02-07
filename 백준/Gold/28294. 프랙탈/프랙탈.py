MOD = 1000000007

N, a = map(int, input().split())

print((N * ((N-1)*pow(N, a, MOD) - (N-2)*pow(N-1, a, MOD)))%MOD)