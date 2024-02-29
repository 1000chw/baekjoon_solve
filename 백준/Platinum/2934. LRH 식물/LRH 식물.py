import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')

n = int(input())
d = defaultdict(int)

tree = [0 for _ in range(400001)]
lazy = [0 for _ in range(400001)]


def update(node, start, end, left, right):
    if right < left:
        return
    if end < left or right < start:
        return

    if left <= start and end <= right:
        if start == end:
            lazy[node] += 1
        else:
            tree[node] += end - start + 1
            lazy[node * 2] += (start + end) // 2 - start + 1
            lazy[node * 2 + 1] += end - (start + end) // 2
        return
    tree[node] += (min(right, end) - max(start, left) + 1)
    if start != end:
        update(node * 2, start, (start + end) // 2, left, right)
        update(node * 2 + 1, (start + end) // 2 + 1, end, left, right)


def find(node, start, end, ind):
    tree[node] += lazy[node]
    answer = lazy[node]
    lazy[node] = 0
    if start == end:
        return answer
    lazy[node * 2] += ((start + end) // 2 - start + 1)*(answer // (end - start + 1))
    lazy[node * 2 + 1] += (end - (start + end) // 2)*(answer // (end - start + 1))
    if (start + end) // 2 >= ind:
        return find(node * 2, start, (start + end) // 2, ind)
    return find(node * 2 + 1, (start + end) // 2 + 1, end, ind)


for _ in range(n):
    l, r = map(int, input().split())
    print(find(1, 1, 100000, l) + find(1, 1, 100000, r))
    update(1, 1, 100000, l+1, r-1)


