N = int(input())
arr = []
for i in range(N):
    x = list(input())
    arr.append(list(map(int, x)))
chk_li = [[0]*N]*N
x_ = [0, 1, 0, -1]
y_ = [1, 0, -1, 0]

def bfs(row, col):
    res = 0
    arr[row][col] = 0
    for i in range(4):
        next_r = row + x_[i]
        next_c = col + y_[i]
        if 0 <= next_c < N and 0 <= next_r < N and arr[next_r][next_c]:
            res += bfs(next_r, next_c)
    return res + 1

result = []
while arr != chk_li:
    for i in range(len(arr)):
        if 1 in arr[i]:
            result.append(bfs(i, arr[i].index(1)))
            break
result.sort()
print(len(result))
for i in result:
    print(i)