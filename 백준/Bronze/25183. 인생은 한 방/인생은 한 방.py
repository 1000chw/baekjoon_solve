import sys
input = sys.stdin.readline

N = int(input())
S = input()
chk = 1
for i in range(1, N):
    if ord(S[i]) - 1 == ord(S[i-1]) or ord(S[i]) + 1 == ord(S[i-1]):
        chk += 1
    else:
        chk = 1
    if chk == 5:
        print('YES')
        break
if chk != 5:
    print('NO')