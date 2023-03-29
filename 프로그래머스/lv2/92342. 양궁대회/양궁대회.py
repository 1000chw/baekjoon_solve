def solution(n, info):
    p_score = 0
    for i in range(10):
        if info[i]:
            p_score += 10-i
    answer = []
    arrows_dict = {}
    res = [-1]
    Gap(info, 0, n, [], res, arrows_dict, 0, p_score)
    if res == [-1]:
        answer.append(-1)
    else:
        answer = list(reversed(list(map(int, list(str(max([int("".join(map(str, reversed(i)))) for i in arrows_dict[res[0]]])))))))
        answer += [0]*(11-len(answer))
    return answer

def Gap(info, i, n, arrows, res, arrows_dict, r_score, p_score):
    if n == 0:
        x = arrows + [0] * (11 - i)
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
        Gap(info, i + 1, 0, [] + arrows, res, arrows_dict, r_score, p_score)
    else:
        arrow = info[i] + 1
        if arrow > n:
            Gap(info, i + 1, n, [] + arrows+[0], res, arrows_dict, r_score, p_score)
            return
        Gap(info, i + 1, n, [] + arrows+[0], res, arrows_dict, r_score, p_score)
        arrows.append(arrow)
        Gap(info, i + 1, n - arrow, [] + arrows, res, arrows_dict,r_score+10-i, p_score-10+i if info[i] else p_score)