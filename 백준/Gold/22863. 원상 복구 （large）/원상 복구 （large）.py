n, k = map(int, input().split())
s = input().split()
d = list(map(lambda x: int(x)-1, input().split()))
visited = [False]*n
res = [''] * n
for i in range(n):
    if not visited[i]:
        li = []
        x = (d[i], i)
        while True:
            if visited[x[0]]:
                break
            li.append(x)
            visited[x[0]] = True
            x = (d[x[0]], x[0])
        mod = len(li)
        for i in range(mod):
            res[li[(i + k - 1) % mod][0]] = s[li[i][1]]
print(' '.join(res))