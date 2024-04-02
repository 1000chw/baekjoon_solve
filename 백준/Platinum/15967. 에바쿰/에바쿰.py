import sys
input = sys.stdin.readline

N, Q1, Q2 = map(int, input().split())
a = [0] + list(map(int, input().split()))

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
    if start == end:
        if left <= start <= right:
            return tree[node]
        return 0
    lazy[node * 2] += ((start + end) // 2 - start + 1) * (answer // (end - start + 1))
    lazy[node * 2 + 1] += (end - (start + end) // 2) * (answer // (end - start + 1))
    if left <= start and end <= right:
        return tree[node]
    elif right < start or left > end:
        return 0
    return find(node * 2 + 1, (start + end) // 2 + 1, end, left, right) + find(node * 2, start, (start + end) // 2,
                                                                               left, right)


def init(node, left, right):
    if left == right:
        tree[node] = a[left]
        return tree[node]
    else:
        mid = (left + right) // 2
        tree[node] = init(node * 2, left, mid) + init(node * 2 + 1, mid + 1, right)
        return tree[node]


init(1, 1, N)

for _ in range(Q1 + Q2):
    query = list(map(int, input().split()))
    if query[1] > query[2]:
        query[1], query[2] = query[2], query[1]
    if query[0] == 1:
        print(find(1, 1, N, query[1], query[2]))
    else:
        update(1, 1, N, query[1], query[2], query[3])
