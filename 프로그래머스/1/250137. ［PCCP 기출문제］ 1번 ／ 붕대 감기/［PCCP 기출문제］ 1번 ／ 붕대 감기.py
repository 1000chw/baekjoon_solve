def solution(bandage, health, attacks):
    answer = 0
    t, x, y = bandage
    h = health
    ba = 0
    for a, d in attacks:
        h = min(health, h + (a-ba-1)//t * y + (a-ba - 1)*x) - d
        if h <= 0:
            return -1
        ba = a
    return h