import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alph = input().split()
alph.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

def solve(cnt, ind, result, chk_v, chk_c):
    if cnt == 0:
        if chk_v >= 1 and chk_c >= 2:
            print(result)
        return 0
    
    for i in range(ind, C-cnt+1):
        if alph[i] in vowel:
            solve(cnt-1, i+1, result+alph[i], chk_v+1, chk_c)
        else:
            solve(cnt-1, i+1, result+alph[i], chk_v, chk_c+1)


solve(L, 0, '', 0, 0)
