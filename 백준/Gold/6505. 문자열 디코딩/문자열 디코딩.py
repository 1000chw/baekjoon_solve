import sys

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    p = list(map(int, input().split()))
    point = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    linked_list = []
    cnt = 0
    for i in p:
        if not visited[i]:
            linked = []
            x = i
            cnt1 = 0
            while True:
                if visited[x]:
                    break
                visited[x] = True
                linked.append(x)
                point[x] = [cnt, cnt1]
                x = p[x-1]
                cnt1 += 1
            linked_list.append(linked)
            cnt += 1
    words = input()
    res = ['.']*n
    for i in range(n):
        ll_len = len(linked_list[point[p[i]][0]])
        res_ind = linked_list[point[p[i]][0]][(point[p[i]][1]+m) % ll_len - 1]-1
        res[res_ind] = words[i]
    print(''.join(res))