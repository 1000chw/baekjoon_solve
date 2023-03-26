def solution(board, skill):
    answer = 0
    x = len(board)
    y = len(board[0])
    arr = [[0]*y for i in range(x)]
    for sk in skill:
        t, x1, y1, x2, y2, d = sk
        if t == 1: 
            d = -d
        arr[x1][y1] += d
        if y2 < y-1: 
            arr[x1][y2+1] -= d
        if x2 < x-1: 
            arr[x2+1][y1] -= d
            if y2 < y-1:
                arr[x2+1][y2+1] += d
    for i in range(0, x):
        for j in range(1, y):
            arr[i][j] += arr[i][j-1]
    for i in range(1, x):
        for j in range(0, y):
            arr[i][j] += arr[i-1][j]
    for i in range(0, x):
        for j in range(0, y):
            if arr[i][j] + board[i][j] > 0:
                answer += 1
    return answer
