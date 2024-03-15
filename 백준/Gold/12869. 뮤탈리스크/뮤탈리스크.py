from collections import deque, defaultdict
from heapq import heappop, heappush
n = int(input())
scv = tuple(map(int, input().split()))
damage = [[], [(9, )], [(9, 3), (3, 9)], [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]]
ld = [0, 1, 2, 6]
cnt_dict = defaultdict(int)

q = [(0, scv)]
while len(q):
    cnt, hp = heappop(q)
    if not hp:
        print(cnt)
        break
    if cnt_dict[hp] != cnt:
        continue
    lhp = len(hp)
    for j in range(ld[lhp]):
        tmp = tuple(hp[i] - damage[lhp][j][i] for i in range(lhp) if hp[i] > damage[lhp][j][i])
        if not cnt_dict[tmp] or cnt_dict[tmp] > cnt + 1:
            q.append((cnt+1, tmp))
            cnt_dict[tmp] = cnt+1
