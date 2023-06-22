import sys
from math import log2, ceil
input = sys.stdin.readline

def makeTree(node, start, end):
    if start == end:
        tree[node] = leaf[start]
    else:
        tree[node] = makeTree(node*2, start, (start+end)//2) + makeTree(node*2+1, (start + end)//2+1, end)
    return tree[node]


def sumTree(node, start, end, left, right):
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return sumTree(node*2, start, (start+end)//2, left, right) + sumTree(node*2+1, (start+end)//2+1, end, left, right)


def updateTree(node, start, end, ind, num):
    if start <= ind <= end:
        tree[node] += num
        if start != end:
            updateTree(node*2, start, (start+end)//2, ind, num)
            updateTree(node * 2+1, (start + end) // 2 + 1, end, ind, num)


N, M, K = map(int, input().split())
leaf = []
tree = [0]*(2**(int(ceil(log2(N)))+1))

for _ in range(N):
    leaf.append(int(input()))

makeTree(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        num = c - leaf[b-1]
        leaf[b-1] = c
        updateTree(1, 0, N-1, b-1, num)
    else:
        print(sumTree(1, 0, N-1, b-1, c-1))
