a, b = map(int, input().split())
answer = 1
while True:
    if b == a:
        print(answer)
        break
    if not b or b % 10 != 1 and b % 2 != 0:
        print(-1)
        break
    elif b % 10 == 1:
        b //= 10
        answer += 1
    else:
        b //= 2
        answer += 1
