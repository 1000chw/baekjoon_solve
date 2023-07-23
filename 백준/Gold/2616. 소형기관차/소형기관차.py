import sys
input = sys.stdin. readline

N = int(input())
train = list(map(int, input().split()))
k = int(input())

train_sum = [0]*(N-k+2)

s = sum(train[:k-1])
for i in range(1, N-k+2):
    s += train[i+k-2]
    train_sum[i] = s
    s -= train[i-1]

dp = [[0]*(N+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(k*i, N-k*(3-i)+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + train_sum[j-k+1])
print(dp[3][-1])
