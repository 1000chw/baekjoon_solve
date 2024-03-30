import sys
input = sys.stdin.readline

def solve(n, s):
    answer = 0
    d = 0
    pre1, pre2 = {0: 1}, {}
    for i in range(n):
        o = ord(s[i]) - ord('A') + 26 if 'A' <= s[i] <= 'Z' else ord(s[i]) - ord('a')
        d ^= 1 << o
        if i % 2:
            if d in pre1.keys():
                answer += pre1[d]
                pre1[d] += 1
            else:
                pre1[d] = 1
            for j in range(52):
                tmp = d ^ (1 << j)
                if tmp in pre2.keys():
                    answer += pre2[tmp]
        else:
            if d in pre2.keys():
                answer += pre2[d]
                pre2[d] += 1
            else:
                pre2[d] = 1
            for j in range(52):
                tmp = d ^ (1 << j)
                if tmp in pre1.keys():
                    answer += pre1[tmp]
    print(answer)

solve(int(input()), input().rstrip())