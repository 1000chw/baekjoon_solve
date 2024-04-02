import sys
from collections import defaultdict, deque
from heapq import heappop, heappush
input = sys.stdin.readline
II = lambda: int(input())
MII = lambda: map(int, input().split())
IR = lambda: input().rstrip()

w = II()
words = []
firsts = defaultdict(list)
boggle = [[]]
for _ in range(w):
    word = IR()
    words.append(word)
    firsts[word[0]].append(word)
tmp = input()

def getPoint(word):
    lw = len(word)
    if lw <= 2:
        return 0
    elif 3 <= lw <= 4:
        return 1
    elif lw == 5:
        return 2
    elif lw == 6:
        return 3
    elif lw == 7:
        return 5
    else:
        return 11

def solve():
    global boggle
    word_f = {wo: 0 for wo in words}
    boggle = [IR() for _ in range(4)]
    tmp = input()
    longest = ''
    point = 0
    for i in range(4):
        for j in range(4):
            for word in firsts[boggle[i][j]]:
                if not word_f[word] and findWord(word, i, j, 0):
                    word_f[word] = 1
                    point += getPoint(word)
                    if len(longest) < len(word):
                        longest = word
                    elif len(longest) == len(word):
                        longest = min(longest, word)
    print(point, longest, sum(word_f.values()))


visited = [False]*16
dx, dy = [0, 0, 1, 1, 1, -1, -1, -1], [1, -1, 0, 1, -1, 0, 1, -1]


def findWord(word, x, y, ind):
    if ind == len(word)-1:
        return True
    answer = False
    visited[x*4+y] = True
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx*4+ny] and word[ind+1] == boggle[nx][ny]:
            answer |= findWord(word, nx, ny, ind+1)
            if answer:
                visited[x*4+y] = False
                return answer
    visited[x*4+y] = False
    return answer


b = II()
for _ in range(b):
    solve()

