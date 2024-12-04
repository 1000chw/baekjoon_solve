import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

squares = [
    ['...',
     '...',
     '...'],
    ['###',
     '###',
     '###']]
triangles = [
    ['###',
     '##.',
     '#..'],
    ['###',
     '.##',
     '..#'],
    ['#..',
     '##.',
     '###'],
    ['..#',
     '.##',
     '###']]

n, m = map(int, input().split())
graph = []

for _ in range(n):
    s1 = input().rstrip()
    s2 = input().rstrip()
    s3 = input().rstrip()
    g = []
    for j in range(m):
        tmp = j*3
        g.append([s1[tmp:tmp+3], s2[tmp:tmp+3], s3[tmp:tmp+3]])
    graph.append(g)

answer = 'YES'
checked = [[False] * m for _ in range(n)]


def findWhiteDiamond(i, j):
    left_x, left_y, right_x, right_y = i, j, i, j+1

    while True:
        if checked[left_x][left_y]:
            return False
        checked[left_x][left_y] = True
        if left_x+1 >= n or left_y-1 < 0 or graph[left_x+1][left_y-1] != triangles[0]:
            break
        left_x += 1
        left_y -= 1

    if right_y < m and graph[right_x][right_y] != triangles[1]:
        return False

    while True:
        if checked[right_x][right_y]:
            return False
        checked[right_x][right_y] = True
        if right_x+1 >= n or right_y+1 >= m or graph[right_x+1][right_y+1] != triangles[1]:
            break
        right_x += 1
        right_y += 1

    for x in range(1, (right_y - j)*2 + 1):
        if x % 2 == 0:
            cx = i + x//2
            cy = j + x//2

            while True:
                checked[cx][cy] = True
                if x == 1:
                    if graph[cx][cy] != triangles[0]:
                        return False
                elif x == (right_y - j)*2:
                    if graph[cx][cy] != triangles[3]:
                        return False
                else:
                    if graph[cx][cy] != squares[0]:
                        return False
                if cx - left_x == cy - left_y:
                    break
                cx += 1
                cy -= 1
        else:
            cx = i + x//2 + 1
            cy = j + x//2
            while True:
                checked[cx][cy] = True
                if cx - left_x == cy - left_y + 1:
                    if graph[cx][cy] != triangles[2]:
                        return False
                    break
                else:
                    if graph[cx][cy] != squares[0]:
                        return False
                cx += 1
                cy -= 1
    return True

def findWhiteRectangle(i, j):
    right = j
    if i != 0 and graph[i-1][j] == squares[0] and checked[i-1][j]:
        return False
    while True:
        if right + 1 >= m or graph[i][right+1] != squares[0]:
            break
        right += 1
    cx, cy = i, j
    while True:
        if cx == n:
            break
        if cy == j:
            if graph[cx][cy] != squares[0]:
                break
            if cx == i and j > 0 and graph[i][j-1] == squares[0]:
                return False
            checked[cx][cy] = True
            if j == right:
                if cy + 1 < m and graph[cx][cy + 1] == squares[0]:
                    return False
                cx += 1
                cy = j - 1
        elif cy == right:
            if graph[cx][cy] != squares[0] or (cy + 1 < m and graph[cx][cy+1] == squares[0]) or checked[cx][cy]:
                return False
            checked[cx][cy] = True
            cx += 1
            cy = j-1
        else:
            if graph[cx][cy] != squares[0] or checked[cx][cy]:
                return False
            checked[cx][cy] = True
        cy += 1

    return True

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    if answer == 'NO':
        break
    for j in range(m):
        g = graph[i][j]
        c = not checked[i][j]
        if not c:
            continue
        elif g == squares[1]:
            checked[i][j] = True
        elif g == triangles[0]:
            if i + 1 >= n or j + 1 >= m:
                answer = 'NO'
                break
            if not findWhiteDiamond(i, j):
                answer = 'NO'
                break
        elif g == squares[0]:
            if not findWhiteRectangle(i, j):
                answer = 'NO'
                break
        elif g in triangles:
            answer = 'NO'
            break
        else:
            checked[i][j] = True
            t = int(g[1][1])
            cnt = 0

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] in triangles:
                    cnt += 1
            if cnt != t:
                answer = 'NO'
                break

print(answer)
