def solution(citations):
    answer = 0
    sorted_citations = list(sorted(citations, reverse=True))
    for i in range(len(citations) - 1):
        if i+1 <= sorted_citations[i] and i+1 >= sorted_citations[i+1]:
            answer = i+1
    if sorted_citations[-1] >= len(sorted_citations):
        answer = len(sorted_citations)
    return answer