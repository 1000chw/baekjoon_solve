from collections import defaultdict

def solution(tickets):
    answer = []
    airport_from = defaultdict(list)
    visited = defaultdict(int)
    for _from, _to in tickets:
        airport_from[_from].append(_to)
        visited[(_from, _to)] += 1
    for _to in airport_from["ICN"]:
        visited[("ICN", _to)] -= 1
        answer.extend(dfs(_to, visited, airport_from, ["ICN", _to], len(tickets)+1))
        visited[("ICN", _to)] += 1
    answer.sort()
    return answer[0]

def dfs(_from, visited, airport_from, track, n):
    if len(track) == n:
        return [track]
    tracks = []
    for _to in airport_from[_from]:
        if visited[(_from, _to)] != 0:
            visited[(_from, _to)] -= 1
            tracks.extend(dfs(_to, visited, airport_from, track+[_to], n))
            visited[(_from, _to)] += 1
    return tracks