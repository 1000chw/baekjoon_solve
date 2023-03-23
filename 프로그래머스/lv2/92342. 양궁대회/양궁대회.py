def solution(n, info):
    answer = []
    arrows_dict = {}
    res = [-1]
    Gap(info, 0, n, [], res, arrows_dict)
    if res == [-1]:
        answer.append(-1)
    else:
        max_gap = sorted(arrows_dict.keys(), reverse=True)[0]
        arrows = [int("".join(map(str, reversed(i)))) for i in arrows_dict[max_gap]]
        ind = 0
        chk = 0
        for i in range(len(arrows)):
            if arrows[i] > chk:
                ind = i
                chk = arrows[i]
        answer = arrows_dict[max_gap][ind]
    return answer

def Gap(info, i, n, arrows, res, arrows_dict):
    if n == 0:
        p_score = 0
        r_score = 0
        x = arrows + [0] * (11 - i)
        for j in range(10):
            if info[j] < x[j]:
                r_score += 10 - j
            elif info[j] > x[j]:
                p_score += 10 - j
        score_gap = r_score - p_score

        if score_gap > 0:
            if score_gap > res[0]:
                arrows_dict[score_gap] = [x]
                res[0] = score_gap
            elif score_gap == res[0]:
                arrows_dict[score_gap].append(x)
        return
    elif i == 10:
        arrows.append(n)
        Gap(info, i + 1, 0, [] + arrows, res, arrows_dict)
    else:
        arrow = info[i] + 1
        if arrow > n:
            arrow = 0
        Gap(info, i + 1, n, [] + arrows+[0], res, arrows_dict)
        arrows.append(arrow)
        Gap(info, i + 1, n - arrow, [] + arrows, res, arrows_dict)