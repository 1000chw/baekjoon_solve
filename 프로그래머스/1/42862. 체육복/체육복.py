def solution(n, lost, reserve):
    answer = 0
    nums = [1]*n
    for l in lost:
        nums[l-1] -= 1
    for r in reserve:
        nums[r-1] += 1

    for i in range(n-1):
        if nums[i] == 0:
            if nums[i+1] == 2:
                nums[i+1] = 1
                nums[i] = 1
        elif nums[i] == 2:
            if nums[i+1] == 0:
                nums[i+1] = 1
                nums[i] = 1
    for n in nums:
        if n:
            answer += 1
    return answer