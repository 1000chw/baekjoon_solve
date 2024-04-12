import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

tree = [0]*(n*4+1)

def init(node, left, right):
    if left == right:
        tree[node] = s[left]
        return tree[node]
    tree[node] = min(init(node * 2, left, (left + right) // 2), init(node * 2 + 1, (left + right) // 2 + 1, right))
    return tree[node]

def update(node, left, right, target, c):
    if left == right:
        tree[node] = c
        return tree[node]
    mid = (left + right) // 2
    if mid >= target:
        tree[node] = min(update(node * 2, left, mid, target, c), tree[node * 2 + 1])
    else:
        tree[node] = min(update(node * 2 + 1, mid + 1, right, target, c), tree[node * 2])
    return tree[node]

def find(node, left, right, st, en):
    if en < left or right < st:
        return 1000000001
    if st <= left and right <= en:
        return tree[node]
    mid = (left + right) // 2
    return min(find(node * 2, left, mid, st, en), find(node * 2 + 1, mid + 1, right, st, en))

init(1, 0, n-1)

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 0, n-1, q[1]-1, q[2])
    else:
        print(find(1, 0, n-1, q[1]-1, q[2]-1))
