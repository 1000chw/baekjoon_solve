import sys
input = sys.stdin.readline

tree = []
n, m = 0, 0
def init(start, end, node):
    if start == end:
        if start <= n:
            tree[node] = 1
        else:
            tree[node] = 0
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node*2) + init(mid + 1, end, node*2 + 1)
    return tree[node]

def sumTree(start, end, left, right, node):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sumTree(start, mid, left, right, node * 2) + sumTree(mid + 1, end, left, right, node * 2 + 1)

def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start == end: return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid+1, end, node * 2 + 1, index, diff)

TL = 800001
IE = 200000

for _ in range(int(input())):
    tree = [0] * TL
    n, m = map(int, input().split())
    watch_list = list(map(int, input().split()))
    cur_index = {i+1: n-i for i in range(n)}
    init(1, IE, 1)
    max_index = n
    for movie in watch_list:
        update(1, IE, 1, cur_index[movie], -1)
        print(sumTree(1, IE, cur_index[movie]+1, max_index, 1), end=" ")
        max_index += 1
        cur_index[movie] = max_index
        update(1, IE, 1, cur_index[movie], 1)
    print()


