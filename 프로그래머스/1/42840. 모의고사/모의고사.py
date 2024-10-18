def solution(answers):
    answer = []
    scores =  [no1(answers), no2(answers), no3(answers)]
    maxScore = max(scores)
    for i in range(3):
        if scores[i] == maxScore:
            answer.append(i+1)
    return answer

def no1(answers):
    pick = [1, 2, 3, 4, 5]
    return getScore(len(pick), len(answers), pick, answers)

def no2(answers):
    pick = [2, 1, 2, 3, 2, 4, 2, 5]
    return getScore(len(pick), len(answers), pick, answers)
    
def no3(answers):
    pick = [3,3,1,1,2,2,4,4,5,5]
    return getScore(len(pick), len(answers), pick, answers)
    
def getScore(p, l, pick, answers):
    score = 0
    for i in range(l):
        score += 1 if pick[i%p] == answers[i] else 0
    return score
    