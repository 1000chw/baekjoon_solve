n, k = map(int, input().split())

res = 0
while bin(n).count('1') > k:
    bottle = bin(n)[::-1].index('1')
    res += 2**bottle
    n += 2**bottle
print(res)
