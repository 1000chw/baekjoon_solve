def solution(record):
    answer = []
    res = []
    id_nick = {}
    id_cur = {}
    for rec in record:
        reco = rec.split()
        
        if len(reco) == 3:
            opt, _id, nick = reco
            if opt == "Enter":
                id_cur[_id] = True
                id_nick[_id] = nick
                res.append([1, _id])
            else:
                id_nick[_id] = nick
        else:
            opt, _id = reco
            res.append([0, _id])

    for chk, id1 in res:
        answer.append(id_nick[id1] + "님이 " + ("들어왔습니다." if chk else "나갔습니다."))
                    
    return answer