visited = []
parents = []
N = 0

def bfs():
    global visited
    global parents
    visited = [0] * 20001
    parents = [[0, '0'] for _ in range(20001)]
    li = []
    li.append(1)
    parents[1][0] = -1
    parents[1][1] = '1'
    visited[1] = 1
    while li:
        tmp = li.pop(0)
        n = [(tmp*10)%N, (tmp*10 + 1)%N]

        for i in range(2):
            if visited[n[i]]:
                continue
            parents[n[i]][0] = tmp
            parents[n[i]][1] = str(i)
            if not n[i]:
                parents[n[i]][1] += '\n'
                return
            visited[n[i]] = 1
            li.append(n[i])

def print_num(n):
    if n == -1:
        return
    print_num(parents[n][0])
    print(parents[n][1], end='')


t = int(input())
for i in range(t):
    visited = []
    parents = []
    N = int(input())
    bfs()
    print_num(0)