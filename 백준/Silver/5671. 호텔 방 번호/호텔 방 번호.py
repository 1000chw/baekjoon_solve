import sys
input = sys.stdin.readline

while 1:
    x = input()
    if x == "":
        break
    start, end = map(int, x.split())
    res = 0
    for i in range(start, end+1):
        num_li = list(str(i))
        if len(num_li) == len(set(num_li)):
            res += 1
    print(res)