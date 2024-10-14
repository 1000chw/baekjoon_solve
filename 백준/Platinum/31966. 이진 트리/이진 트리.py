import sys
input = sys.stdin.readline

n = int(input())
nodes = [1] * (n+1)
count = [1] * (n+1)
l_count = [1] * (n+1)
r_count = [1] * (n+1)

for i in range(1, n+1):
    left, right = map(int, input().split())
    l_count[i] = l_count[left] + l_count[right] + nodes[right] - 1
    r_count[i] = r_count[right] + r_count[left] + nodes[left] - 1
    nodes[i] = nodes[left] + nodes[right]
    count[i] = count[left] + count[right] + r_count[left]*nodes[right] + l_count[right]*nodes[left] - 1
    print(count[i])
