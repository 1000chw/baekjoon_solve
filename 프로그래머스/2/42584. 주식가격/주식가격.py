def solution(prices):
    answer = [0]*len(prices)
    stack = [(0, prices[0])]
    for i in range(1, len(prices)):
        while stack and stack[-1][1] > prices[i]:
            x, p = stack.pop()
            answer[x] = i - x
        stack.append((i, prices[i]))
    while stack:
        x, p = stack.pop()
        answer[x] = len(prices) - x - 1
    return answer