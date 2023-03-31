def solution(N, stages):
    answer = []
    dic = {i:[0, 0] for i in range(1, N+1)}
    for s in stages:
        for i in range(1, s):
            dic[i][1] += 1
        if s != N+1:
            dic[s][0] += 1
            dic[s][1] += 1
    res = [[i,dic[i][0]/dic[i][1] if dic[i][1] else 0] for i in dic.keys()]
    k = sorted(res, key = lambda x: (-x[1], x[0]))
    answer = [i[0] for i in k]
    return answer