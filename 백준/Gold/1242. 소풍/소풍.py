n, k, m = map(int, input().split())
ind = 1
answer = 0
while n:
    ind = (ind + k - 1) % n
    if not ind:
        ind = n
    answer += 1
    if ind == m:
        break
    n -= 1
    if ind < m:
        m -= 1
print(answer)
