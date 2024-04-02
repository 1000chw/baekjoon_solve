import sys
input = sys.stdin.readline
II = lambda: int(input())
MII = lambda: map(int, input().split())
IR = lambda: input().rstrip()

tree = [0 for _ in range(4000001)]
lazy = [0 for _ in range(4000001)]


def update(node, start, end, left, right, s):
    if right < left:
        return
    if end < left or right < start:
        return

    if left <= start and end <= right:
        if start == end:
            lazy[node] += s
        else:
            tree[node] += (end - start + 1) * s
            lazy[node * 2] += ((start + end) // 2 - start + 1) * s
            lazy[node * 2 + 1] += (end - (start + end) // 2) * s
        return
    tree[node] += (min(right, end) - max(start, left) + 1) * s
    if start != end:
        update(node * 2, start, (start + end) // 2, left, right, s)
        update(node * 2 + 1, (start + end) // 2 + 1, end, left, right, s)


def find(node, start, end, left, right):
    tree[node] += lazy[node]
    answer = lazy[node]
    lazy[node] = 0
    if left <= start and end <= right:
        return tree[node]
    elif right < start or left > end:
        return 0
    lazy[node * 2] += ((start + end) // 2 - start + 1)*(answer // (end - start + 1))
    lazy[node * 2 + 1] += (end - (start + end) // 2)*(answer // (end - start + 1))

    return find(node * 2 + 1, (start + end) // 2 + 1, end, left, right) + find(node * 2, start, (start + end) // 2, left, right)


N, Q1, Q2 = MII()
a = list(MII())
for i in range(N):
    update(1, 1, N, i+1, i+1, a[i])

for _ in range(Q1 + Q2):
    query = list(MII())
    if query[0] == 1:
        print(find(1, 1, N, query[1], query[2]))
    else:
        update(1, 1, N, query[1], query[2], query[3])
