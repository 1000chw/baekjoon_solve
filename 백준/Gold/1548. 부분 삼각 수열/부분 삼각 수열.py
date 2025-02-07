n = int(input())
nums = list(map(int, input().split()))
nums.sort()

answer = 0
start = 0

for i in range(n):
    if i - start + 1 < 3:
        answer = max(answer, i-start+1)
    else:
        if nums[start] + nums[start+1] > nums[i]:
            answer = max(answer, i-start+1)
        else:
            for j in range(start, i):
                if nums[j] + nums[j+1] > nums[i]:
                    start = j
                    break

print(answer)