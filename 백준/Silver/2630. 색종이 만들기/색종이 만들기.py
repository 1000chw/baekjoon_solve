import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    li = list(map(int, input().split()))
    arr.append(li)

res = [0, 0]


def solve(_rt, _rb, _ct, _cb):
    tmp = set()
    for x in range(_rt, _rb+1):
        for y in range(_ct, _cb+1):
            tmp.add(arr[x][y])
    if len(tmp) == 1:
        if list(tmp)[0]:
            res[1] += 1
        else: res[0] += 1
    else:
        solve(_rt, (_rt+_rb)//2, _ct, (_ct+_cb)//2)
        solve(_rt, (_rt+_rb)//2, (_ct+_cb)//2 + 1, _cb)
        solve((_rt+_rb)//2 + 1, _rb, _ct, (_ct+_cb)//2)
        solve((_rt+_rb)//2 + 1, _rb, (_ct+_cb)//2 + 1, _cb)
        return


solve(0, N-1, 0, N-1)

print(res[0])
print(res[1])