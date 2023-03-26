def dfs(n, info, graph, n_sheep, n_wolf, visited, res, trace):
    chk = False
    if info[n] == 0 and n not in trace:
        n_sheep += 1
        visited = {n: True}
        trace.append(n)
        res.append(n_sheep)
        chk = True
    elif info[n] == 1 and n not in trace:
        n_wolf += 1
        trace.append(n)
        chk = True
    if n_wolf == n_sheep:
        del visited[n]
        trace.pop()
        return
    for i in graph[n]:
        if i not in visited:
            visited[i] = True
            dfs(i, info, graph, n_sheep, n_wolf, visited, res, trace)
    del visited[n]
    if chk:
        trace.pop()
    return


def solution(info, edges):
    answer = 0
    graph = {}
    for i, j in edges:
        if i in graph:
            graph[i].append(j)
        else:
            graph[i] = [j]
        if j in graph:
            graph[j].append(i)
        else:
            graph[j] = [i]
    visited = {}
    res = []
    trace = []
    dfs(0, info, graph, 0, 0, visited, res, trace)
    answer = max(res)
    return answer