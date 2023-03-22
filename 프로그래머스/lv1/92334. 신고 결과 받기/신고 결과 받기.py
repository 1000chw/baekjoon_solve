def solution(id_list, report, k):
    answer = []
    reports = {i:[] for i in id_list}
    banned = {i:0 for i in id_list}
    for ids in report:
        id1, id2 = ids.split()
        if id2 not in reports[id1]:
            reports[id1].append(id2)
            banned[id2] += 1
    for id in id_list:
        cnt = 0
        for rep_id in reports[id]:
            if banned[rep_id] >= k:
                cnt += 1
        answer.append(cnt)
    return answer