N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, list(input()))))

x_ = [0, 1, 0, -1]
y_ = [1, 0, -1, 0]

def dfs(row, col):
    res = 0
    arr[row][col] = 0
    for i in range(4):
        next_r = row + x_[i]
        next_c = col + y_[i]
        if 0 <= next_c < N and 0 <= next_r < N and arr[next_r][next_c]:
            res += dfs(next_r, next_c)
    return res + 1

result = []
for i in range(N):
	for j in range(N):
		if arr[i][j]: 
			result.append(dfs(i, j))
result.sort()
print(len(result))
for i in result:
    print(i)