import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)

costs = list(map(int, input().split()))

memo = [0]*n

def solve(node):
    if not tree[node]:
        return costs[node]
    childs_costs = [solve(i) for i in tree[node]]
    max_sum = 0
    for cost in childs_costs:
        if cost > 0:
            max_sum += cost
    return costs[node] + max_sum

print(solve(0))
