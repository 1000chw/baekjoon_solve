import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

tree = [0]*(n*4+1)

def init(node, left, right):
    if left == right:
        tree[node] = s[left]
        return tree[node]
    tree[node] = init(node * 2, left, (left + right) // 2) + init(node * 2 + 1, (left + right) // 2 + 1, right)
    return tree[node]

def update(node, left, right, target, c):
    if left == right:
        tree[node] += c
        return
    tree[node] += c
    mid = (left + right) // 2
    if mid >= target:
        update(node * 2, left, mid, target, c)
    else:
        update(node * 2 + 1, mid + 1, right, target, c)

def find(node, left, right, target):
    if left == right:
        return left + 1
    if tree[node * 2] >= target:
        return find(node * 2, left, (left + right) // 2, target)
    else:
        return find(node * 2 + 1, (left + right) // 2 + 1, right, target - tree[node * 2])

init(1, 0, n-1)

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, 0, n-1, q[1]-1, q[2])
    else:
        print(find(1, 0, n-1, q[1]))