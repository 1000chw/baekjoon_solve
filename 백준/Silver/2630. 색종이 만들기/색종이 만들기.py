import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    arr.append(li)

res = [0, 0]


def solve(_rt, _rb, _ct, _cb, res):
    if all(arr[x][y] == 1 for y in range(_ct, _cb+1) for x in range(_rt, _rb+1)):
        res[1] += 1
        return
    elif all(arr[x][y] == 0 for y in range(_ct, _cb+1) for x in range(_rt, _rb+1)):
        res[0] += 1
        return
    else:
        solve(_rt, (_rt+_rb)//2, _ct, (_ct+_cb)//2, res)
        solve(_rt, (_rt+_rb)//2, (_ct+_cb)//2 + 1, _cb, res)
        solve((_rt+_rb)//2 + 1, _rb, _ct, (_ct+_cb)//2, res)
        solve((_rt+_rb)//2 + 1, _rb, (_ct+_cb)//2 + 1, _cb, res)
        return


solve(0, N-1, 0, N-1, res)

print(res[0])
print(res[1])

