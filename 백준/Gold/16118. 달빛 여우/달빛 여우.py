from heapq import heappush, heappop
import sys
rl = sys.stdin.readline
INF = int(1e9)


def dik_fox():
    dist = [INF for _ in range(N+1)]
    dist[1] = 0
    q = []
    heappush(q, (dist[1], 1))

    while q:
        cd, ci = heappop(q)
        if dist[ci] < cd:
            continue
        for vd, vi in G[ci]:
            nd = cd + vd
            if nd < dist[vi]:
                dist[vi] = nd
                heappush(q, (dist[vi], vi))
    return dist


def dik_wolf():
    # dist[0] 빠르게 도착 / dist[1] 느리게 도착
    dist = [[INF] * (N+1) for _ in range(2)]
    dist[1][1] = 0
    q = []
    heappush(q, (dist[1][1], 1, False))

    while q:
        cd, ci, cf = heappop(q)
        if cf and dist[0][ci] < cd:
            continue
        elif not cf and dist[1][ci] < cd:
            continue

        for vd, vi in G[ci]:
            if cf:  # 빠르게 도착했다면, 느리게 출발
                nd = cd + (vd * 2)
                if nd < dist[1][vi]:
                    dist[1][vi] = nd
                    heappush(q, (dist[1][vi], vi, False))
            else:  # 느리게 도착했다면, 빠르게 출발
                nd = cd + (vd // 2)
                if nd < dist[0][vi]:
                    dist[0][vi] = nd
                    heappush(q, (dist[0][vi], vi, True))

    return dist


N, M = map(int, rl().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, rl().split())
    G[a].append((d * 2, b))
    G[b].append((d * 2, a))

fox = dik_fox()
wolf = dik_wolf()

answer = 0
for i in range(1, N+1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1
print(answer)