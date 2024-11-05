import sys
input = sys.stdin.readline

n = int(input())

classroom = [[0] * (n+2) for _ in range(n+2)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
like_dict = {}

for _ in range(n*n):
    ns = list(map(int, input().split()))
    cur_n = ns.pop(0)
    like_dict[cur_n] = ns
    max_likes, max_empty = 0, 0
    x, y = 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if classroom[i][j]:
                continue
            likes, empty = 0, 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 == nx or 0 == ny or n+1 == nx or n+1 == ny:
                    continue
                elif classroom[nx][ny] == 0:
                    empty += 1
                elif classroom[nx][ny] in ns:
                    likes += 1
            if likes > max_likes:
                max_likes = likes
                max_empty = empty
                x, y = i, j
            elif likes == max_likes and empty > max_empty:
                max_empty = empty
                x, y = i, j
            elif x == y == 0:
                max_likes = likes
                max_empty = empty
                x, y = i, j
    classroom[x][y] = cur_n

answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        x = classroom[i][j]
        cnt = 0
        for k in range(4):
            if classroom[i+dx[k]][j+dy[k]] in like_dict[x]:
                cnt += 1
        answer += 10**cnt // 10

print(answer)