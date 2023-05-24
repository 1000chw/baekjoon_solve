wall = [[[]]]

def check(x, y, a, b):
    global wall
    if x < 0 or y < 0 or (not b and not wall[x][y][a]):
        return True
    if a:
        if wall[x][y - 1][0] or wall[x + 1][y - 1][0] or (x - 1 >= 0 and wall[x - 1][y][1] and wall[x + 1][y][1]):
            return True
    else:
        if y == 0 or wall[x][y - 1][0] or (x-1 >= 0 and wall[x - 1][y][1]) or wall[x][y][1]:
            return True
    return False

def solution(n, build_frame):
    global wall
    answer = []
    wall = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b:
            if check(x, y, a, b):
                wall[x][y][a] = 1
        else:
            if a:
                wall[x][y][1] = 0
                if not (check(x-1, y, 1, b) and check(x, y, 0, b) and check(x+1, y, 1, b) and check(x+1, y, 0, b)):
                    wall[x][y][1] = 1
            else:
                wall[x][y][0] = 0
                if not (check(x, y+1, 0, b) and check(x, y+1, 1, b) and check(x-1, y+1, 1, b)):
                    wall[x][y][0] = 1

    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if wall[i][j][k]:
                    answer.append([i, j, k])
    answer.sort()
    return answer
