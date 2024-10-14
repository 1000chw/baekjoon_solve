import sys
input = sys.stdin.readline
MOD = 1000000007
n = int(input())
nodes = [1] * (n+1)
count = [1] * (n+1)
l_count = [1] * (n+1)
r_count = [1] * (n+1)

for i in range(1, n+1):
    left, right = map(int, input().split())
    l_count[i] = (l_count[left] + l_count[right] + nodes[right] - 1) % MOD
    r_count[i] = (r_count[right] + r_count[left] + nodes[left] - 1) % MOD
    nodes[i] = (nodes[left] + nodes[right]) % MOD
    count[i] = (count[left] + count[right] + r_count[left]*nodes[right] + l_count[right]*nodes[left] - 1) % MOD
    print(count[i])
