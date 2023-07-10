from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(1000000)


def preorder(left, right, p_left, p_right, c):
    if left > right or p_left > p_right:
        return
    root = postorder[p_right]
    root_ind = index_li[root]
    print(root, end=' ')
    preorder(left, root_ind-1, p_left, root_ind-c-1, c)
    preorder(root_ind+1, right, root_ind-c, p_right-1, c+1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
index_li = [0]*(n+1)
for i in range(n):
    index_li[inorder[i]] = i
preorder(0, n-1, 0, n-1, 0)
